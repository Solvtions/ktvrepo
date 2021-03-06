import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red][B]Kritik TV Wizard[/B][/COLOR]'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'http://kritiktv.net/ktv/Texts/autobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'YouTube Help Videos'
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
# Text file for roms and emus
ROMPACK        = 'http://'
EMUAPKS        = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://kritiktv.net/ktv/Images/builds.png'
ICONMAINT      = 'http://kritiktv.net/ktv/Images/maintain.png'
ICONSPEED      = 'http://kritiktv.net/ktv/Images/speedtest.png'
ICONAPK        = 'http://kritiktv.net/ktv/Images/apk.png'
ICONRETRO      = 'http://kritiktv.net/ktv/Images/retro.png'
ICONADDONS     = 'http://kritiktv.net/ktv/Images/addon.png'
ICONYOUTUBE    = 'http://kritiktv.net/ktv/Images/youtube.png'
ICONSAVE       = 'http://kritiktv.net/ktv/Images/save.png'
ICONTRAKT      = 'http://kritiktv.net/ktv/Images/trakt.png'
ICONREAL       = 'http://kritiktv.net/ktv/Images/debrid.png'
ICONLOGIN      = 'http://kritiktv.net/ktv/Images/login.png'
ICONCONTACT    = 'http://kritiktv.net/ktv/Images/contact.png'
ICONSETTINGS   = 'http://kritiktv.net/ktv/Images/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '-'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'red'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B]([COLOR '+COLOR2+'])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing KriTiK TV Wizard.\r\n\r\n Contact us at:  support@kritiktv.net'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://kritiktv.net/ktv/Images/contact.png'
CONTACTFANART  = 'http://kritiktv.net/repo2/Wallpaper/System/ktvsystem.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://kritiktv.net/ktv/Texts/autobuilds.txt'
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
REPOZIPURL     = 'http://kritiktv.net/ktv/repo'
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
HEADERMESSAGE  = 'Kritik TV Wizard'
# url to image if using Image 500x50(Width can vary but height of image needs to be 50px)
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'http://kritiktv.net/ktv/Images/notify.jpg'
#########################################################