import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red][B]Kritik TV Wizard[/B][/COLOR]'
BUILDERNAME    = 'Kritik'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repository.ktvrepo', 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = 'http://kritiktv.net/ktv/Texts/builds.txt'
UPDATECHECK    = 0
APKFILE        = 'http://kritiktv.net/ktv/Texts/apks.txt'
YOUTUBETITLE   = 'Kritik TV' 
YOUTUBEFILE    = 'http://'
ADDONFILE      = 'http://'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'red'
EXIT_BUTTON_COLOR = 'white'
#Highlight outline for lists
HIGHLIGHT_LIST = 'orange'
##No TXT file Banner
NO_TXT_FILE = 'red'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'white'
#All other buttons
OTHER_BUTTONS_TEXT = 'orange'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'redorange'


#Description text title color
DES_T_COLOR = 'red'
#Description color
DESCOLOR = 'white'

#Wizard title name and verion color
WIZTITLE = 'Kritik TV Wizard'
WIZTITLE_COLOR = 'red'
VERTITLE_COLOR = 'white'
VER_NUMBER_COLOR = 'red'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'red'
COLOR2         = 'white'
COLOR3         = 'orange'
COLOR4         = 'snow'
COLOR5         = 'redorange'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://'
ICONMAINT      = 'http://'
ICONAPK        = 'http://'
ICONADDONS     = 'http://'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'http://'
ICONSETTINGS   = 'http://'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '-'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing KriTiK TV Wizard.\r\n\r\nContact us at:  support@kritiktv.net'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'http://kritiktv.net/repo2/Wallpaper/System/ktvsystem.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://kritiktv.net/ktv/Texts/builds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'repository.ktvrepo'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/Solvtions/ktvrepo/master/repository.ktvrepo/addons.xml'
# Url to folder zip is located in
REPOZIPURL     =  'http://kritiktv.net/ktv/repo'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://kritiktv.net/ktv/Texts/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
# Font size of header
FONTHEADER     = 'Font13'
HEADERMESSAGE  = 'Kritik TV Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'http://kritiktv.net/ktv/Images/notify.jpg'
############################    #############################