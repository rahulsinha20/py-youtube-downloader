; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{13B33AFB-C7DE-4A84-8D4F-080C12F3C231}
AppName=Py-Youtube-Downloader
AppVersion=2.0
;AppVerName=Py-Youtube-Downloader 2.0
AppPublisher=Abhi Laboratories
AppPublisherURL=http://code.google.com/p/py-youtube-downloader/
AppSupportURL=http://code.google.com/p/py-youtube-downloader/
AppUpdatesURL=http://code.google.com/p/py-youtube-downloader/
DefaultDirName=c:\Py-Youtube-Downloader
DefaultGroupName=Py-Youtube-Downloader
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1
[Files]
Source: "C:\dev\apps\py-utube\dist\YouTubeDownloaderApp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\LIBEAY32.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\phonon4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\PyQt4.Qt.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\PyQt4.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\PyQt4.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\PyQt4.QtNetwork.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\PyQt4.QtWebKit.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\python27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\QtCore4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\QtGui4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\QtNetwork4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\QtWebKit4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\sip.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\SSLEAY32.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\dev\apps\py-utube\dist\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
;Source: "C:\dev\apps\py-utube\build\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\dev\apps\py-utube\dist\imageformats\*"; DestDir: "{app}/imageformats"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\dev\apps\py-utube\dist\Resources\*"; DestDir: "{app}/Resources"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Py-Youtube-Downloader"; Filename: "{app}\YouTubeDownloaderApp.exe"
Name: "{group}\{cm:UninstallProgram,Py-Youtube-Downloader}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Py-Youtube-Downloader"; Filename: "{app}\YouTubeDownloaderApp.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YouTubeDownloaderApp.exe"; Description: "{cm:LaunchProgram,Py-Youtube-Downloader}"; Flags: nowait postinstall skipifsilent

