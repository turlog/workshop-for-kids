## Konfiguracja środowiska

Stworzenie środowiska Conda na podstawie pliku `environment.yml`:

    conda env create -f environment.yml --force

Aktywacja środowiska:

    conda activate workshop-for-kids

Instalacja przykładowego pakietu w trybie deweloperskim:

    pip install -e package

## Cykl rozwoju oprogramowania

1. Napisanie testu (edycja `test_hello.py`) dla nowej funkcjonalności.
2. Uruchomienie testów (`pytest`) - test kończy się błędem.
3. Napisanie kodu (edycja `hello.py`) implementującego funkcjonalność.
4. Uruchomienie testów (`pytest`) - test kończy się sukcesem.
5. Uruchomienie statycznej analizy (`pylint` / `flake8` / `mypy`).
6. Poprawienie jakości kodu zgodnie z sugestiami narzędzi.
7. Uruchomienie testów (`pytest`) - test kończy się sukcesem.
8. Aktualizacja dokumentacji.
