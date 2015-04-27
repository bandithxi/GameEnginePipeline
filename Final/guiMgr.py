import Tkinter as tk
import time
import sys
import math
import ogre.renderer.OGRE as ogre
import os

class GuiMgr:
	
    def __init__( self, engine ):
        self.engine = engine

    def init( self ):
        self.overlayMgr = False
        self.levelSelect = False
        self.hudMgr = False
		
    def displaySplash( self ):	
        self.gfxMgr = self.engine.gfxMgr

        root = tk.Tk()
        imageList = ["media/overlay/SplashStart.jpeg"]
        introMusic = "sound.ogg"
        
        root.overrideredirect(True)
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
        root.config(cursor='none')
        canvas = tk.Canvas(root, height=height, width=width, bg="white")
        canvas.pack()

        displayList = []

        for imgPath in imageList:
            img = tk.PhotoImage( file = imgPath )
            displayList.append( img )
        
        for guiElement in displayList:
            canvas.delete(tk.ALL)
            canvas.create_image(width/2, height/2, image=guiElement)
            canvas.update()
            sound = self.soundMgr.createSound("introMusic", introMusic)
            sound.setGain(1)
            self.soundMgr.destroySound("introMusic")
            sound.play()
            time.sleep(.30)
        
        # show the splash screen for 5000 milliseconds then destroy
        root.after(0, self.gfxMgr.createRenderWindow)
        root.after(0, root.destroy)
        root.mainloop()

    def displayMainMenu( self ):
        self.entityMgr = self.engine.entityMgr
    
        # Load the font
        font = ogre.FontManager.getSingleton().getResourceIterator()
        
        while( font.hasMoreElements() ):
            font.getNext().load()
    
        self.overlayMgr = ogre.OverlayManager.getSingleton()
    
        # Create Main Menu BGD
        self.overlay = self.overlayMgr.create( "MainMenuBGD" )

        # Create a panel
        self.panel = self.overlayMgr.createOverlayElement( "Panel", "Menu" )
        self.panel.setPosition( 0, 0 )
        self.panel.setDimensions( 1, 1)
        self.panel.setMaterialName( "Splash" )
        
        # Create a button panel
        self.panel2 = self.overlayMgr.createOverlayElement( "Panel", "Buttons" )
        self.panel2.setPosition( .05, .5 )
        self.panel2.setDimensions( .25, .35 )
        self.panel2.setMaterialName( "clearPanel" )
        
        # Create level panel
        self.panel3 = self.overlayMgr.createOverlayElement( "Panel", "LevelButtons" )
        self.panel3.setPosition( .363, .5 )
        self.panel3.setDimensions( .25, .35 )
        self.panel3.setMaterialName( "clearPanel" )

            # Create Instructions Panel
        self.panel4 = self.overlayMgr.createOverlayElement( "Panel", "InstructionScreen" )
        self.panel4.setPosition( .118, .12 )
        self.panel4.setDimensions( .75, .75 )
        self.panel4.setMaterialName( "Instructions" )
        
        # Create Credits Panel
        self.panel5 = self.overlayMgr.createOverlayElement( "Panel", "CreditScreen" )
        self.panel5.setPosition( .118, .12 )
        self.panel5.setDimensions( .75, .75 )
        self.panel5.setMaterialName( "Credits" )
        
        # Title
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Title" )
        self.text.setPosition( .01, .11 )
        self.text.setDimensions( .5, .5 )
        self.text.setCaption( "Footy" )    
        self.text.setCharHeight(.1)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((0.0, 0.0, 0.0))
        self.text.setColourBottom((0.0, 0.0, 0.0))
        self.panel.addChild( self.text )
 
        # Title
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Titley" )
        self.text.setPosition( .25, .11 )
        self.text.setDimensions( .5, .5 )
        self.text.setCaption( "y" )    
        self.text.setCharHeight(.1)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((0.0, 0.0, 0.0))
        self.panel.addChild( self.text )


        # Start Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Start" )
        self.text.setPosition( 0.05, 0.05)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "New Game" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 1, 1, 1 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )
        
        # Instructions Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Instructions" )
        self.text.setPosition( 0.05, 0.10)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "Instructions" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 1, 1, 1 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )

        # Credits Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Credits" )
        self.text.setPosition( 0.05, 0.15)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "Credits" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 1, 1, 1 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )

        # Add the panel to the overlay
        self.overlay.add2D( self.panel )
        self.overlay.add2D( self.panel2 )
        self.overlay.add2D( self.panel3 )
        self.overlay.add2D( self.panel4 )
        self.overlay.add2D( self.panel5 )
        
        # Show the overlay
        #self.overlay.show()
        self.overlay.hide()

        level = self.overlayMgr.getOverlayElement( "LevelButtons" )
        level.hide()

        instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
        instructions.hide()

        credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
        credits.hide()        
    
    def displayHud (self):


        self.hudMgr = ogre.OverlayManager.getSingleton()
        self.hud = self.hudMgr.getByName( "HUD/HUD_Info" )
        self.hud.hide()
        # Create the HUD

        self.hud2 = self.hudMgr.create( "HUD" )

        # Populate the HUD 
        self.hudPanel = self.overlayMgr.createOverlayElement( "Panel", "PanelName" )
        self.hudPanel.setPosition( 0, 0 )
        self.hudPanel.setDimensions( 1, 1)
        self.hudPanel.setMaterialName( "Examples/Hud" )


        # Team One
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Team Name One" )
        self.text.setPosition( .025, .055 )
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "USA" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )

 
        # Team Two
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Team Name Two" )
        self.text.setPosition( .025, .1225 )
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "Mexico" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )

        # Score 1 
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Score - Team One" )
        self.text.setPosition( .2575, .055 )
        self.text.setDimensions( 1, 1 )
        scoreOne = "0"
        self.text.setCaption( scoreOne )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )

        # Score 2 
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Score - Team Two" )
        self.text.setPosition( .2575, .1225 )
        self.text.setDimensions( 1, 1 )
        scoreTwo = "0"
        self.text.setCaption( scoreTwo )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )


        # Time 
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Time" )
        self.text.setPosition( .885, .055 )
        self.text.setDimensions( 1, 1 )
        Time = "5:00"
        self.text.setCaption( Time )    
        self.text.setCharHeight(.03)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )
        self.hud2.add2D( self.hudPanel )
        self.hud2.show()
        #self.hud.hide()

    def tick(self, dt): 
        
        time = str(self.engine.gameMgr.gameTime / 60) + ":" +str(self.engine.gameMgr.gameTime % 60) 
        self.text = self.hudMgr.getOverlayElement("Time")
        self.text.setCaption(time)
        
        score = str(self.engine.gameMgr.scoreOne)
        self.text = self.hudMgr.getOverlayElement("Score - Team Two")
        self.text.setCaption(score)

        
        score = str(self.engine.gameMgr.scoreTwo)
        self.text = self.hudMgr.getOverlayElement("Score - Team One")
        self.text.setCaption(score)

        pass

