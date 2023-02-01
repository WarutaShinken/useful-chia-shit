set name=chia
set version=1.5.0

set binpath=%localappdata:\=\\%\\%name%-blockchain\\app-%version%\\resources\\app.asar.unpacked\\daemon

::Uncomment if the client you're targetting is based on Chia 1.5.1 or higher.
::set binpath=%localappdata:\=\\%\\Programs\\%name%\\resources\\app.asar.unpacked\\daemon

taskkill /f /im %name%.exe
WMIC Process Where "ExecutablePath='%binpath%\\daemon.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_crawler.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_farmer.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_full_node.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_harvester.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_introducer.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_seeder.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_timelord.exe'" Call Terminate
WMIC Process Where "ExecutablePath='%binpath%\\start_wallet.exe'" Call Terminate