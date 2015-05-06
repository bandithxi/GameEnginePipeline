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

        # Create main panel
        self.panel = self.overlayMgr.createOverlayElement( "Panel", "Menu" )
        self.panel.setPosition( 0, 0 )
        self.panel.setDimensions( 1, 1)
        self.panel.setMaterialName( "Splash" )
        
        # Create a button panel
        self.panel2 = self.overlayMgr.createOverlayElement( "Panel", "Buttons" )
        self.panel2.setPosition( .05, .5 )
        self.panel2.setDimensions( .25, .35 )
        self.panel2.setMaterialName( "clearPanel" )
       
       ###### PLAYER 1 #####
        ### Main Flag ###
        # Create a red flag panel
        self.panelFlagRed = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Red")
        self.panelFlagRed.setPosition( .35, .16 )
        self.panelFlagRed.setDimensions ( .31, .32 )
        self.panelFlagRed.setMaterialName ( "FlagRed" )

        # Create a blue flag panel
        self.panelFlagBlue = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Blue")
        self.panelFlagBlue.setPosition( .35, .16 )
        self.panelFlagBlue.setDimensions ( .31, .32 )
        self.panelFlagBlue.setMaterialName ( "FlagBlue" )

        # Create a yellow flag panel
        self.panelFlagYellow = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Yellow")
        self.panelFlagYellow.setPosition( .35, .16 )
        self.panelFlagYellow.setDimensions ( .31, .32 )
        self.panelFlagYellow.setMaterialName ( "FlagYellow" )

        # Create a green flag panel
        self.panelFlagGreen = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Green")
        self.panelFlagGreen.setPosition( .35, .16 )
        self.panelFlagGreen.setDimensions ( .31, .32 )
        self.panelFlagGreen.setMaterialName ( "FlagGreen" )

        # Create a purple flag panel
        self.panelFlagPurple = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Purple")
        self.panelFlagPurple.setPosition( .35, .16 )
        self.panelFlagPurple.setDimensions ( .31, .32 )
        self.panelFlagPurple.setMaterialName ( "FlagPurple" )

        ### Mini Flag Left ###

        # Create a red mini flag
        self.panelFlagRedL = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Red-L")
        self.panelFlagRedL.setPosition( .23, .24 )
        self.panelFlagRedL.setDimensions ( .139, .139 )
        self.panelFlagRedL.setMaterialName ( "FlagRed" )
        
       ###### PLAYER 2 ######
        ### Main Flag ### 
        # Create a red flag panel
        self.panelFlagRedP2 = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Red-P2")
        self.panelFlagRedP2.setPosition( .35, .65 )
        self.panelFlagRedP2.setDimensions ( .31, .32 )
        self.panelFlagRedP2.setMaterialName ( "FlagRed" )

        # Create a blue flag panel
        self.panelFlagBlueP2 = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Blue-P2")
        self.panelFlagBlueP2.setPosition( .35, .65 )
        self.panelFlagBlueP2.setDimensions ( .31, .32 )
        self.panelFlagBlueP2.setMaterialName ( "FlagBlue" )

        # Create a Yellow flag panel
        self.panelFlagYellowP2 = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Yellow-P2")
        self.panelFlagYellowP2.setPosition( .35, .65 )
        self.panelFlagYellowP2.setDimensions ( .31, .32 )
        self.panelFlagYellowP2.setMaterialName ( "FlagYellow" )

        # Create a Green flag panel
        self.panelFlagGreenP2 = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Green-P2")
        self.panelFlagGreenP2.setPosition( .35, .65 )
        self.panelFlagGreenP2.setDimensions ( .31, .32 )
        self.panelFlagGreenP2.setMaterialName ( "FlagGreen" )

        # Create a Purple flag panel
        self.panelFlagPurpleP2 = self.overlayMgr.createOverlayElement ( "Panel", "Flag-Purple-P2")
        self.panelFlagPurpleP2.setPosition( .35, .65 )
        self.panelFlagPurpleP2.setDimensions ( .31, .32 )
        self.panelFlagPurpleP2.setMaterialName ( "FlagPurple" )



        # Create team panel
        self.panel3 = self.overlayMgr.createOverlayElement( "Panel", "LevelButtons" )
        self.panel3.setPosition( 0, 0 )
        self.panel3.setDimensions( 1, 1 )
        self.panel3.setMaterialName( "TeamSelect" )

        # Create Instructions Panel
        self.panel4 = self.overlayMgr.createOverlayElement( "Panel", "InstructionScreen" )
        self.panel4.setPosition( 0, 0 )
        self.panel4.setDimensions( 1, 1 )
        self.panel4.setMaterialName( "Instructions" )
        
        # Create Credits Panel
        self.panel5 = self.overlayMgr.createOverlayElement( "Panel", "CreditScreen" )
        self.panel5.setPosition( 0, 0 )
        self.panel5.setDimensions( 1, 1 )
        self.panel5.setMaterialName( "Credits" )

        # Create a button panel
        self.panel6 = self.overlayMgr.createOverlayElement( "Panel", "BackButton" )
        self.panel6.setPosition( 0.0, 0.925 )
        self.panel6.setDimensions( .1, .075 )
        #self.panel6.setMaterialName( "clearPanel" )
        
        # Start Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Start" )
        self.text.setPosition( 0.05, 0.05)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "NEW GAME" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 0, 0, 0 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )
        
        # Instructions Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Instructions" )
        self.text.setPosition( 0.05, 0.10)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "INSTRUCTIONS" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 0, 0, 0 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )

        # Credits Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "Credits" )
        self.text.setPosition( 0.05, 0.15)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "CREDITS" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 0, 0, 0 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )

        
        # Selection Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "TeamSelect" )
        self.text.setPosition( 0.05, 0.20)
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "TEAM SELECT" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColour( ( 0, 0, 0 ) )
        self.text.setSpaceWidth( .01 )
        self.panel2.addChild( self.text )

        # Back Button
        self.text = self.overlayMgr.createOverlayElement( "TextArea", "BackSelect" )
        self.text.setPosition( 0.01, 0.02  )
        self.text.setDimensions( .05, .05 )
        self.text.setCaption( "Back" )    
        self.text.setCharHeight(.03)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.panel6.addChild( self.text )


        # Add the panel to the overlay
        self.overlay.add2D( self.panel )
        self.overlay.add2D( self.panel2 )
        self.overlay.add2D( self.panel3 )
        self.overlay.add2D( self.panel4 )
        self.overlay.add2D( self.panel5 )
        self.overlay.add2D( self.panel6 )
        self.overlay.add2D( self.panelFlagRed )
        self.overlay.add2D( self.panelFlagBlue )
        self.overlay.add2D( self.panelFlagYellow )
        self.overlay.add2D( self.panelFlagPurple )
        self.overlay.add2D( self.panelFlagGreen )
        self.overlay.add2D( self.panelFlagRedL )
        self.overlay.add2D( self.panelFlagRedP2 )
        self.overlay.add2D( self.panelFlagBlueP2 )
        self.overlay.add2D( self.panelFlagYellowP2 )
        self.overlay.add2D( self.panelFlagPurpleP2 )
        self.overlay.add2D( self.panelFlagGreenP2 )

        # grabbed window height and width
        self.windowWidth  = self.engine.gfxMgr.renderWindow.getWidth()
        self.windowHeight = self.engine.gfxMgr.renderWindow.getHeight()
        print "renderwindow x: ", self.windowWidth, "y: ", self.windowHeight

        # grabbed top left x and y axis of button panel
        self.buttonBoxX = self.panel2.getLeft() * self.windowWidth
        self.buttonBoxY = self.panel2.getTop() * self.windowHeight
        #print "buttonBox x: ", self.buttonBoxX, "y: ", self.buttonBoxY

        # find start button position
        self.buttonStartX = self.buttonBoxX + (self.windowWidth  * 0.025)
        self.buttonStartY = self.buttonBoxY + (self.windowHeight * 0.025)
        #print "start: ", self.buttonStartX, self.buttonStartY
        
        # find instruction, credits, team selection button position
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

        back = self.overlayMgr.getOverlayElement( "BackButton" )
        back.hide()
        
        self.flagRed = self.overlayMgr.getOverlayElement( "Flag-Red" )
        self.flagRed.hide()

        self.flagBlue = self.overlayMgr.getOverlayElement( "Flag-Blue" )
        self.flagBlue.hide()

        self.flagYellow = self.overlayMgr.getOverlayElement( "Flag-Yellow" )
        self.flagYellow.hide()

        self.flagGreen = self.overlayMgr.getOverlayElement( "Flag-Green" )
        self.flagGreen.hide()

        self.flagPurple = self.overlayMgr.getOverlayElement( "Flag-Purple" )
        self.flagPurple.hide()

        self.flagRedL = self.overlayMgr.getOverlayElement( "Flag-Red-L" )
        self.flagRedL.hide()

        self.flagRedP2 = self.overlayMgr.getOverlayElement( "Flag-Red-P2" )
        self.flagRedP2.hide()

        self.flagBlueP2 = self.overlayMgr.getOverlayElement( "Flag-Blue-P2" )
        self.flagBlueP2.hide()

        self.flagYellowP2 = self.overlayMgr.getOverlayElement( "Flag-Yellow-P2" )
        self.flagYellowP2.hide()

        self.flagGreenP2 = self.overlayMgr.getOverlayElement( "Flag-Green-P2" )
        self.flagGreenP2.hide()

        self.flagPurpleP2 = self.overlayMgr.getOverlayElement( "Flag-Purple-P2" )
        self.flagPurpleP2.hide()
    
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
        self.text.setPosition( .125, .07 )
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "USA" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((1.0, 1.0, 1.0))
        self.text.setColourBottom((1.0, 1.0, 1.0))
        self.hudPanel.addChild( self.text )

 
        # Team Two
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Team Name Two" )
        self.text.setPosition( .125, .13 )
        self.text.setDimensions( 1, 1 )
        self.text.setCaption( "Mexico" )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((0.0, 0.0, 0.0))
        self.text.setColourBottom((0.0, 0.0, 0.0))
        self.hudPanel.addChild( self.text )

        # Score 1 
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Score - Team One" )
        self.text.setPosition( .2375, .065 )
        self.text.setDimensions( 1, 1 )
        scoreOne = "0"
        self.text.setCaption( scoreOne )    
        self.text.setCharHeight(.025)
        self.text.setFontName("Fifa15Font")
        self.text.setColourTop((0.0, 0.0, 0.0))
        self.text.setColourBottom((0.0, 0.0, 0.0))
        self.hudPanel.addChild( self.text )

        # Score 2 
        self.text = self.hudMgr.createOverlayElement( "TextArea", "Score - Team Two" )
        self.text.setPosition( .2375, .135 )
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
        self.text.setPosition( .26, .09 )
        self.text.setDimensions( 1, 1 )
        Time = "5:00"
        self.text.setCaption( Time )    
        self.text.setCharHeight(.06)
        self.text.setFontName("MyriadPro")
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
            self.flagYellow.show()
            self.flagYellowP2.show()
            self.teamSelect = False
        
        # instructions screen
        if self.engine.gameMgr.instructionsCheck == True and self.engine.gameMgr.startCheck == False:
            instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
            backButton  = self.overlayMgr.getOverlayElement("BackButton")
            instructions.show()
            backButton.show() 
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()       
            self.engine.gameMgr.instructionsCheck = False     
        
        # credit screen
        if self.engine.gameMgr.creditsCheck == True and self.engine.gameMgr.startCheck == False:
            credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
            backButton  = self.overlayMgr.getOverlayElement("BackButton")
            backButton.show()
            credits.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()
            self.engine.gameMgr.creditsCheck = False   

        # back to main 
        if self.engine.gameMgr.backCheck == True and self.engine.gameMgr.startCheck == False:
            menu = self.overlayMgr.getOverlayElement( "Menu" )
            instructions = self.overlayMgr.getOverlayElement( "InstructionScreen" )
            credits = self.overlayMgr.getOverlayElement( "CreditScreen" )
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            teams = self.overlayMgr.getOverlayElement( "LevelButtons" )
            backButton  = self.overlayMgr.getOverlayElement("BackButton")
            
            teams.hide()
            credits.hide()
            instructions.hide()
            menu.show()          
            buttons.show()
            backButton.hide()
            self.flagYellow.hide()
            self.flagBlue.hide()
            self.flagRed.hide()
            self.flagGreen.hide()
            self.flagPurple.hide()
            self.flagRedL.hide()
            self.flagRedP2.hide()
            self.flagBlueP2.hide()
            self.flagRedP2.hide()
            self.flagGreenP2.hide()
            self.flagPurpleP2.hide()
            self.engine.gameMgr.creditsCheck = False  
            self.engine.gameMgr.instructionsCheck = False 
            self.engine.gameMgr.teamCheck = False
            self.teamSelect = False
            self.engine.gameMgr.backCheck = False
            self.engine.gameMgr.startCheck = False
         
        if self.engine.gameMgr.teamCheck == True and self.engine.gameMgr.startCheck == False:
            backButton  = self.overlayMgr.getOverlayElement("BackButton")
            backButton.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement( "Buttons" )
            buttons.hide()
            self.engine.gameMgr.teamCheck = False 

        pass
        
    def updateScore(self):
        score = str(self.engine.gameMgr.scoreOne)
        self.text = self.hudMgr.getOverlayElement("Score - Team Two")
        self.text.setCaption(score)

        
        score = str(self.engine.gameMgr.scoreTwo)
        self.text = self.hudMgr.getOverlayElement("Score - Team One")
        self.text.setCaption(score)
   
    def updateTime(self): 
        tempTime = ( self.engine.gameMgr.gameTime % 60 )

        if tempTime >= 0 and tempTime <= 9:
                tempTime = "0" + str (tempTime)

        time = str(self.engine.gameMgr.gameTime / 60) + ":" + str (tempTime) 
        self.text = self.hudMgr.getOverlayElement("Time")
        self.text.setCaption(time)
