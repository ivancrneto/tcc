from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.new_project import Ui_NewProject
from ui.choose_sequences import Ui_ChooseSequences
from ui.matrices import Ui_Matrices
from ui.generate_matrices import Ui_GenerateMatrices
from ui.image_dialog import Ui_ImageDialog
import os
import operator
import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot
from matplotlib import image as mpimg
import numpy

class NewProject(QDialog, Ui_NewProject):
    '''
    Class with a dialog to the user fill the
    data for a new project
    '''
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.connect(self.browse_project_button, SIGNAL('clicked()'), self.browse_project_directory)
        self.connect(self.browse_database_button, SIGNAL('clicked()'), self.browse_database_directory)
        #self.move((screen.width() - size.width())/2,
        #          (screen.height() - size.height())/2)
    
    def accept(self):
        if self.project_name.text() and self.project_path.text() and self.database_path.text():
            self.accepted = True
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
        
    #TODO: change to become only one function
    def browse_project_directory(self):
        self.project_path.setText(QFileDialog.getExistingDirectory(self, 'Choose the directory',
            os.path.expanduser('~')))
            
    def browse_database_directory(self):
        self.database_path.setText(QFileDialog.getExistingDirectory(self, 'Choose the directory',
            os.path.expanduser('~')))
            
            
class ChooseSequences(QDialog, Ui_ChooseSequences):
    '''
    Class with a dialog to the user choose the sequences to generate
    the similarity matrix
    '''
    def __init__(self, sequences_map, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        
        self.selected_cells = []
        
        self.sequence_table.tabledata, self.sequence_table.inputmap = self.handle_sequences(sequences_map)
        self.create_table()
        self.sequence_table.setColumnWidth(9, 300)
        
    def handle_sequences(self, sequences_map):
        #TODO: change to handle when a organism has more than one sequence
        sequences_view = []
        sequences_input_map = {}
        for organism, sequences in sequences_map.items():
            for sequence in sequences:
                sequences_view.append([
                    sequence.gi,
                    ', '.join(sequence.accessions),
                    sequence.locus,
                    sequence.version,
                    sequence.community,
                    str(sequence.organism),
                    sequence.description,
                    sequence.file,
                    sequence.alphabet,
                    str(sequence.code),
                ])
                sequences_input_map[sequence.locus] = sequence
        return sequences_view, sequences_input_map

    def create_table(self):
        header = ['Gi', 'Accessions', 'Locus', 'Version', 'Community', 'Organism', 
                'Description', 'File', 'Alphabet', 'Code']
        
        table_model = GenericTableModel(self.sequence_table.tabledata, header, self) 
        self.sequence_table.setModel(table_model)
        
        self.sequence_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.sequence_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        self.sequence_table.setMinimumSize(400, 300)

        self.sequence_table.setShowGrid(False)

        font = QFont("Times New Roman", 10)
        self.sequence_table.setFont(font)

        vh = self.sequence_table.verticalHeader()
        vh.setVisible(False)

        hh = self.sequence_table.horizontalHeader()
        hh.setStretchLastSection(True)

        self.sequence_table.resizeColumnsToContents()

        nrows = len(self.sequence_table.tabledata)
        for row in xrange(nrows):
            self.sequence_table.setRowHeight(row, 18)

        self.sequence_table.setSortingEnabled(True)
        
        #QObject.connect(self.sequence_table, SIGNAL("clicked(QModelIndex)"), self.test_clicked)
        
    def selected_sequences(self):
        sequences_list = []
        for cell_id in self.selected_cells:
            if cell_id in self.sequence_table.inputmap:
                sequences_list.append(self.sequence_table.inputmap[cell_id])
                
        return sequences_list
    
    def accept(self):
        selected_cells = self.sequence_table.selectionModel().selectedRows(2)
        while selected_cells:
            self.selected_cells.append('%s' % selected_cells.pop().data(Qt.DisplayRole).toString())
        
        self.accepted = True
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
    
    
#got from: http://www.saltycrane.com/blog/2007/12/pyqt-43-qtableview-qabstracttablemodel/
class GenericTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.headerdata = headerdata
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.arraydata[0]) 
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        return QVariant(self.arraydata[index.row()][index.column()]) 

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class Matrices(QDialog, Ui_Matrices):
    '''
    Class with a dialog to the user operate with matrices
    '''
    def __init__(self, project, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        self.project = project
        self.matrix_tableview.tabledata = self.get_matrices()
        self.create_table()
        self.generate_matrices_button.setFocusPolicy(Qt.NoFocus)
        self.network_graph_button.setFocusPolicy(Qt.NoFocus)
        self.color_matrix_graph_button.setFocusPolicy(Qt.NoFocus)
        self.export_matrices_button.setFocusPolicy(Qt.NoFocus)
        self.analyse_thresholds_button.setFocus(Qt.OtherFocusReason)
        
        self.connect(self.generate_matrices_button, SIGNAL('clicked()'), self.generate_matrices)
        self.connect(self.color_matrix_graph_button, SIGNAL('clicked()'), self.color_matrix_graph)
        
    def get_matrices(self):
        adj_matrices = self.project.get_adjacency_matrices()
        nbh_matrices = self.project.get_neighbourhood_matrices()
        
        matrices_dict = []
        for threshold in range(0, 101):
            if threshold in adj_matrices:
                adj_generated = 'Yes'
            else:
                adj_generated = ''
            if threshold in nbh_matrices:
                nbh_generated = 'Yes'
                if nbh_matrices[threshold].rearranged:
                    nbh_generated += ', Rearranged: Yes'
                else:
                    nbh_generated += ', Rearranged: No'
            else:
                nbh_generated = ''
            matrices_dict.append([threshold, adj_generated, nbh_generated])
        
        matrices_dict.reverse()
        return matrices_dict
        
    def generate_matrices(self):
        generate_matrices_dialog = GenerateMatrices()
        generate_matrices_dialog.exec_()
        if generate_matrices_dialog.accepted:
            self.project.generate_adjacency_matrices(generate_matrices_dialog.adj_matrix_gen)
            self.project.generate_neighbourhood_matrices(generate_matrices_dialog.nbh_matrix_gen)
            #TODO: should not be here
            self.project.bio_handler.matrices = [self.project.similarity_matrix] + \
                self.project.adjacency_matrices + self.project.neighbourhood_matrices
                
            
            self.project.save_project()
            
            self.matrix_tableview.tabledata = self.get_matrices()
            self.create_table()
            
    def color_matrix_graph(self):
        selected_cells = self.matrix_tableview.selectionModel().selectedRows(0)
        selected_cells_data = []
        while selected_cells:
            selected_cells_data.append('%s' % selected_cells.pop().data(Qt.DisplayRole).toString())
        
        threshold = int(selected_cells_data[0])
        nbh_matrix = self.project.get_neighbourhood_matrix(threshold)
        
        if nbh_matrix != None:
            image_dialog = ImageDialog(self, image='color matrix', nbh_matrix=nbh_matrix)
            image_dialog.exec_()
        else:
            print 'Neighbourhood Matrix None'
    
    def create_table(self):
        header = ['Threshold', 'Adjacency Matrix', 'Neighbourhood Matrix']
        
        table_model = GenericTableModel(self.matrix_tableview.tabledata, header, self) 
        self.matrix_tableview.setModel(table_model)
        
        self.matrix_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.sequence_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        self.matrix_tableview.setMinimumSize(400, 300)

        self.matrix_tableview.setShowGrid(False)

        font = QFont("Times New Roman", 10)
        self.matrix_tableview.setFont(font)

        vh = self.matrix_tableview.verticalHeader()
        vh.setVisible(False)

        hh = self.matrix_tableview.horizontalHeader()
        hh.setStretchLastSection(True)

        self.matrix_tableview.resizeColumnsToContents()

        nrows = len(self.matrix_tableview.tabledata)
        for row in xrange(nrows):
            self.matrix_tableview.setRowHeight(row, 18)

        self.matrix_tableview.setSortingEnabled(True)
        self.matrix_tableview.sortByColumn(0, Qt.AscendingOrder)
        self.matrix_tableview.setColumnWidth(0, 120)
        
    def closeEvent(self, event):
        print 'testing close event'
        self.emit(SIGNAL("closed()"))


class ImageDialog(QDialog, Ui_ImageDialog):
    '''
    Class with a dialog to the user view images in general
    '''
    def __init__(self, parent=None, **kwargs):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        
        self.dpi = 100
        self.fig = Figure((7.0, 5.2), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        
        self.navbar_layout.addWidget(self.mpl_toolbar)
        
        if 'image' in kwargs:
            if kwargs['image'] == 'color matrix':
                self.show_color_matrix(kwargs['nbh_matrix'])

    def show_color_matrix(self, nbh_matrix):
        nbh_matrix_data = nbh_matrix.data
        #TODO: try to choose better colors
        #for i in range(0, len(nbh_matrix_data)):
        #    for j in range(0, len(nbh_matrix_data[i])):
        #        print nbh_matrix_data[i][j]
        #        new_number = var * nbh_matrix_data[i][j]
        #        nbh_matrix_data[i][j] = [new_number, new_number, new_number]

        img = numpy.array(nbh_matrix_data)
        #TODO: add colorbar
        #self.fig.colorbar()
        #pyplot.colorbar()
        imgplot = self.axes.imshow(img)
        imgplot.set_cmap('spectral')
        imgplot.set_interpolation('nearest')

    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))

class GenerateMatrices(QDialog, Ui_GenerateMatrices):
    '''
    Class with a dialog to the user generate matrices
    '''
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        
        self.rearrange_checkbox.setDisabled(True)
        
        self.connect(self.nbh_matrix_checkbox, SIGNAL('stateChanged(int)'), self.nbh_mat_checkbox)
        
        self.accepted = False
            
    def nbh_mat_checkbox(self, state):
        if state == Qt.Checked:
            self.rearrange_checkbox.setEnabled(True)
        else:
            self.rearrange_checkbox.setDisabled(True)
        
    def accept(self):
        if self.threshold_input.text():
            self.accepted = True
            if '-' in self.threshold_input.text():
                begin = int(self.threshold_input.text().split('-')[0])
                end = int(self.threshold_input.text().split('-')[1])
            else:
                begin = end = int(self.threshold_input.text())
            
            self.adj_matrix_gen = {}
            if self.adj_matrix_checkbox.checkState() == Qt.Checked:
                self.adj_matrix_gen = {
                    'begin': begin,
                    'end': end,
                }
            
            if self.rearrange_checkbox.checkState() == Qt.Checked:
                rearrange = True
            else:
                rearrange = False
            
            self.nbh_matrix_gen = {}
            if self.nbh_matrix_checkbox.checkState() == Qt.Checked:
                self.nbh_matrix_gen = {
                    'begin': begin,
                    'end': end,
                    'rearrange': rearrange,
                }
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        print 'testing close event 2'
        self.emit(SIGNAL("closed()"))











































