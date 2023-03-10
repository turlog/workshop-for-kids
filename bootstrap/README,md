## Bootstrap środowiska

Wszystkie polecenia uruchamiamy w PowerShell z uprawnieniami administratora w katalogu `C:\WINDOWS\system32`

Kopiujemy pliki `*ps1` do katalogu `C:\WINDOWS\system32`.

1. `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
2. `& .\bootstrap1.ps1` - konfiguruje język polski systemu + `winget`
3. reboot
4. `winget list` - akceptujemy licencję
5. `& .\bootstrap2.ps1` - instaluje pakiety
6. reboot
7. `& .\bootstrap2.ps1` - dokańcza instalację (akualizuje condę)
8. trzeba przeklikać domyślny język VS Code

## Konfiguracja środowiska

Zainstalowany jest Git i Conda (w ścieźce, każdy terminal PowerShell będzie to miał). Pracujemy w terminalu wewnątrz VS Code ewentualniew Windows Terminal. Na pulpicie są skróty do Scratcha, VS Code oraz link otwierający repozytorium. Użytkownicy mają uprawnienia administracyjne i robią co zechcą.