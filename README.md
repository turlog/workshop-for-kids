# Poznaj Pythona!
### _I zr�b to jak prawdziwy profesjonalista_

W ramach warsztat�w chcieliby�my przedstawi� Wam nie tylko popularny j�zyk programowania, ale pokaza� te� jak mo�e wygl�da� spos�b rozwi�zania zadania w spos�b, w jaki na co dzie� mierz� si� profesjonalni programi�ci.

Opr�cz rozwi�zywania przygotowanych dla Was zada� chcieliby�my poruszy� nast�puj�ce tematy i znale�� odpowiedzi na kilka pyta�:
- Czym jest algorytm? Jak mo�emy go zapisywa�?
- Czym jest j�zyk programowania i kod programu?
- Jak napisa� i uruchomi� algorytm w Pythonie na przyk�adzie rysowania figury geometrycznej.
- Czym jest funkcja, po co jej u�ywamy?
- Na czym polega testowanie? 
- Z jakich narz�dzi na co dzie� u�ywaj� profesjonalni programi�ci w pracy?
- W jaki spos�b mo�emy dodawa� zmiany do istniej�cego projektu?

Stawiamy na praktyk�, dlatego cz�� teoretyczn� ograniczymy do minimum (to nie lekcje w szkole!) i od razu dostaniecie od nas sprz�t i praktyczne zadanie!

### Grafika ��wiowa

Jest to klasyka, klasyk, z kt�r� mogli�cie mie� ju� styczno�� r�wnie� przy okazji innych j�zyk�w. Grafika ��wiowa pozwala nam porusza� po ekranie programu symptatycznym ��wikiem, kt�ry w trakcie przesuwania si�, mo�e pozostawia� za sob� �lad, dzi�ki czemu mo�emy pokierowa� nim i zaprogramowa� jego ruch, rysuj�c podobnie jak d�ugopisem lub o��wkiem na kartce.

Waszym zadaniem b�dzie uzupe�nienie przygotowanego wst�pnie pakietu Pythonowego, korzystaj�c z przyk�ad�w kt�re udost�pnimy razem z pakietem. Aby wykona� zadanie, skorzystajcie z poni�szych wskaz�wek:

- W pierwszej kolejno�ci pami�taj, �eby poprawnie zdoby� wst�pny kod z pakietem oraz przyk�adami, najlepiej b�dzie je�eli sklonujesz repozytorium dost�pne publicznie pod adresem https://github.com/turlog/workshop-for-kids (nie wiesz czym jest tajemniczy program git? Zapytaj prowadz�cego!),
- W repozytorium znajdziesz dwa katalogi, katalog "package" to ten, w kt�rym oczekujemy Twojego rozwi�zania, w katalogu "examples" znajdziesz przyk�ady kodu wraz z pozostawionymi TODO, czyli elementami, kt�re musimy uzupe�ni�,
- Zacznij od uruchomienia skrypt�w z przyk�adowym kodem oraz przyjrzenia si� zapisanym tam algorytmom, zacznij od pliku square.py, gdzie pokazano przyk�ad narysowania kwadratu (Czy masz pomys� jak mo�naby w taki sam spos�b narysowa� tr�jk�t r�wnoboczny?), nast�pnie przyjrzyj si� co znajdziemy w figure.py (tam znajdziemy te� pierwszy TODO i funkcj� kt�r� chcieliby�my mie� w gotowym pakiecie), ostatecznie zaprogramujemy ��wiowy wy�cig, kt�ry znajdziemy w pliku race.py,
- Aby uruchomi� skrypt Pythonowy mo�emy skorzysta� z wiersza polece� i polecenia `python <nazwa skryptu>` lub wykorzystuj�c dost�pne IDE (zintegrowane �rodowisko deweloperskie), zach�camy do skorzystania z drugiego sposobu,
- Pami�taj, �e gotowy pakiet powinien zawiera� nie tylko kod produkcyjny, ale r�wnie� zestaw test�w automatycznych, kt�re pomagaj� w wyszukiwaniu b��d�w oraz sprawdzenia stworzonego rozwi�zania. Szablon do pisania test�w znajdziesz w pliku `test_hello.py` swoje testy mo�ecie dopisa� w analogiczny spos�b, a ca�y zestaw uruchomi� przy u�yciu komendy `pytest` (lub naszego IDE ;)),
- Je�eli macie ju� konto na GitHubie mo�ecie stworzy� Pull Request z Waszym rozwi�zaniem, je�eli nie macie jeszcze konta, wystarczy �e przeniesiecie Wasze rozwi�zanie na osobnego brancha, sprawdzimy w IDE co uda�o si� przygotowa� ;)
- I najwa�niejsza zasada, je�eli macie z czymkolwiek problem, nie wiecie jak zacz��, co� nie dzia�a, pami�tajcie �e jeste�my tutaj dla Was i chcemy pom�c Wam w zadaniu (to te� nasza rola jako bardziej do�wiadczonych!), to bardzo wa�ne, �eby�cie nie bali si� poprosi� o pomoc (profesjonali�ci te� to robi�!).

Powodzenia!

### Dla szybkich i ambitnych

Przygotowa�e� ju� ca�y pakiet i by�o to bardzo proste? Zerknij do plik�w `lsystem.py` i `test_lsystem.py` i spr�buj rozgry�� co robi ten przyk�ad i jak mo�emy zmusi� algorytm do narysowania czego� innego (profesjonali�ci na co dzie� du�o wi�cej kodu musz� przeczyta� i zrozumie�, ni� napisa� ;)
