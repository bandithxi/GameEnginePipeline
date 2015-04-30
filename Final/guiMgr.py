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
        self.teamSelect = False

        #button positions
        self.buttonBoxX = 0.0
        self.buttonBoxY = 0.0
        self.buttonStartX = 0.0
        self.buttonStartY = 0.0
        self.buttonInstructY = 0.0
        self.buttonCreditsY = 0.0
        self.buttonTeamSelY = 0.0
        self.windowWidth = 0.0
        self.windowHeight = 0.0

    def createMainMenu( self ):
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
        
        # Create team panel
        self.panel3 = self.overlayMgr.createOverlayElement( "Panel", "LevelButtons" )
        self.panel3.setPosition( 0, 0 )
        self.panel3.setDimensions( 1, 1 )
        self.panel3.setMaterialName( "TeamSelect" )

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

        
        # Credits Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "TeamSelect" )
        self.text.setPosition( 0.05, 0.20)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "Team Selection" )    
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

        # grabbed window height and width
        self.windowWidth  = self.engine.gfxMgr.renderWindow.getWidth()
        self.windowHeight = self.engine.gfxMgr.renderWindow.getHeight()
        #print "renderwindow x: ", self.windowWidth, "y: ", self.windowHeight

        # grabbed top left x and y axis of button panel
        self.buttonBoxX = self.panel2.getLeft() * self.windowWidth
        self.buttonBoxY = self.panel2.getTop() * self.windowHeight
        #print "buttonBox x: ", self.buttonBoxX, "y: ", self.buttonBoxY

        # calculate start button position
        self.buttonStartX = self.buttonBoxX + (self.windowWidth  * 0.025)
        self.buttonStartY = self.buttonBoxY + (self.windowHeight * 0.025)
        #print "start: ", self.buttonStartX, self.buttonStartY
        
        # calculate instruction, credits, team selection button position
        self.buttonInstructY = self.buttonBoxY + (self.windowHeight * 0.075)
        self.buttonCreditsY = self.buttonBoxY + (self.windowHeight * 0.125)
        self.buttonTeamSelectionY = self.buttonBoxY + (self.windowHeight * 0.175)

        # Show the overlay
        self.overlay.show()
        #self.overlay.hide()

        level = self.overlayMgr.getOverlayElement( "LevelButtons" )
        level.hide()

        instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
        instructions.hide()

        credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
        credits.hide()   
    
    def createHud (self):
        self.hudMgr = ogre.OverlayManager.getSingleton()
        #self.hud = self.hudMgr.getByName( "HUD/HUD_Info" )
        #self.hud.hide()
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
        #self.hud2.show()
        #self.hud.hide()

    def tick(self, dt): 
        self.updateTime()
        self.updateScore()

        if self.engine.gameMgr.teamCheck == True and self.engine.gameMgr.startCheck == False:
            #self.teamSelect = True
            buttons = self.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()
            teams = self.overlayMgr.getOverlayElement( "LevelButtons" )
            teams.show()
            self.teamSelect = False
        
        
        if self.engine.gameMgr.instructionsCheck == True and self.engine.gameMgr.startCheck == False:
            instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
            instructions.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()       
            self.engine.gameMgr.instructionsCheck = False     
        
        if self.engine.gameMgr.creditsCheck == True and self.engine.gameMgr.startCheck == False:
            credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
            credits.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()
            self.engine.gameMgr.creditsCheck = False   

        #invisible button, please make visible and move 
        if self.engine.gameMgr.backCheck == True and self.engine.gameMgr.startCheck == False:
            menu = self.overlayMgr.getOverlayElement( "Menu" )
            instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
            credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            teams = self.overlayMgr.getOverlayElement( "LevelButtons" )
            
            teams.hide()
            credits.hide()
            instructions.hide()
            menu.show()          
            buttons.show()
            self.engine.gameMgr.creditsCheck = False  
            self.engine.gameMgr.instructionsCheck = False 
            self.engine.gameMgr.teamCheck = False
            self.teamSelect = False
            self.engine.gameMgr.backCheck == False
            self.engine.gameMgr.startCheck == False
         
        if self.engine.gameMgr.startCheck == True: #and self.teamSelect == True:
            #self.teamSelect = True
            buttons = self.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()
            
            #self.engine.gameMgr.teamCheck = False

        pass
        
    def updateScore(self):
        score = str(self.engine.gameMgr.scoreOne)
        self.text = self.hudMgr.getOverlayElement("Score - Team Two")
        self.text.setCaption(score)

        
        score = str(self.engine.gameMgr.scoreTwo)
        self.text = self.hudMgr.getOverlayElement("Score - Team One")
        self.text.setCaption(score)
   
    def updateTime(self):
        time = str(self.engine.gameMgr.gameTime / 60) + ":" +str(self.engine.gameMgr.gameTime % 60) 
        self.text = self.hudMgr.getOverlayElement("Time")
        self.text.setCaption(time)
