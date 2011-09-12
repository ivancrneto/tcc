from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.new_project import Ui_NewProject
from ui.choose_sequences import Ui_ChooseSequences
import os
import operator

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
        
        table_model = SequencesTableModel(self.sequence_table.tabledata, header, self) 
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
class SequencesTableModel(QAbstractTableModel): 
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
    
    
