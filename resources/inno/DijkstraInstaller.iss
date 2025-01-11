[Setup]
AppName=Dijkstra
AppVersion=0.1.0
DefaultDirName={pf}\Dijkstra
DefaultGroupName=Dijkstra
OutputBaseFilename=DijkstraInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\khevp\PycharmProjects\pythonProject\dist\Dijkstra.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Dijkstra"; Filename: "{app}\Dijkstra.exe"
Name: "{userdesktop}\Dijkstra"; Filename: "{app}\Dijkstra.exe"; Tasks: desktopicon

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; \
    ValueType: string; ValueName: "DijkstraAutorun"; ValueData: """{app}\Dijkstra.exe"""; Flags: uninsdeletevalue

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Run]
Filename: "{app}\Dijkstra.exe"; Description: "{cm:LaunchProgram,Dijkstra}"; Flags: nowait postinstall skipifsilent
