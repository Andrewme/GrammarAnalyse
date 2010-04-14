import gtk

from algorithms import Algorithms

algo = Algorithms()

class MainForm():
    def MainWindow(self):
        window = gtk.Window()
        window.set_title('Grammar Analyse')
        window.maximize()

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(self._BuildMenuBar(), 0)

        '''Here I'am post result'''
        self.label_answer = gtk.Label("")
        vbox.pack_start(self.label_answer, 0)

        textEditor = gtk.TextView()
        self.textbuffer = textEditor.get_buffer()
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add(textEditor)
        vbox.add(sw)

        window.add(vbox)
        window.show_all()

        window.connect("destroy", gtk.main_quit)
        gtk.main()
        print "Quit"

    #Private methods
    def _LoadFromTextEdit(self):
        return self.textbuffer.get_text(self.textbuffer.get_start_iter(), \
                                                 self.textbuffer.get_end_iter())

    def _UnproductiveUnTerminals(self, widget):
        unproductive = []

        unproductive = algo.UnNTerminals(self._LoadFromTextEdit())
        if len(unproductive) == 0:
            self.label_answer.set_text("Unproductive set: empty")
        else:
            self.label_answer.set_text("Unproductive set: " + str(unproductive))

        return None

    def _Follow(self):
        algo.Follow(self._LoadFromTextEdit)

        return None

    def _BuildMenuBar(self):
        menuBar = gtk.MenuBar()

        fileMenu = gtk.Menu()
        menuFile = gtk.MenuItem('File')
        menuFile.set_submenu(fileMenu)
        itemOpen = gtk.ImageMenuItem(gtk.STOCK_OPEN)
        itemQuit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        fileMenu.append(itemOpen)
        fileMenu.append(itemQuit)

        itemQuit.connect("activate", gtk.main_quit)

        funcMenu = gtk.Menu()
        menuFunctions = gtk.MenuItem('Functions')
        menuFunctions.set_submenu(funcMenu)
        itemUnTerminals = gtk.MenuItem('Unproductive unterminals')
        itemFollow = gtk.MenuItem('Follow(A)')
        #itemSearchSet = gtk.MenuItem('Search set')
        funcMenu.append(itemUnTerminals)
        funcMenu.append(itemFollow)
        #funcMenu.append(itemSearchSet)

        itemUnTerminals.connect("activate", self._UnproductiveUnTerminals)
        itemFollow.connect("activate", self._Follow)

        aboutMenu = gtk.Menu()
        menuAbout = gtk.MenuItem('About')
        menuAbout.set_submenu(aboutMenu)

        menuBar.append(menuFile)
        menuBar.append(menuFunctions)
        #TODO Create about menu.
        #menuBar.append(menuAbout)

        return menuBar
