<h1> Классификация клеток крови на 7 групп + артефакты </h1> 

<h4>Цель работы: </h4>
<p>
Данная работа направлена на классификацию 7 типов лейкоцитов и артефактов. 
В ходе исследования мы будем обучать и тестировать ML-модель.
< / p>

<h4>Описание данных:</h4>

<p>
Данные содержат информацию о различных параметрах клеток крови.  
Например, площадь клетки, площадь цитоплазмы, площадь ядра, количество ядер, количество гранул, радиус клетки, радиус ядра и т.д...
< / p>

<h4>План работы:</h4>

<p>
1. Загрузка данных
2. Анализ данных 
3. Модель обучения
4. Результаты
< / p>

<br>
Загрузка данных 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7560 entries, 0 to 7559
Data columns (total 36 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   CArea          7560 non-null   float64
 1   CFFact         7560 non-null   float64
 2   CPolar         7560 non-null   float64
 3   NArea          7560 non-null   float64
 4   NFFact         7560 non-null   float64
 5   NPolar         7560 non-null   float64
 6   NCCave         7560 non-null   float64
 7   NCaveMaxPiece  7560 non-null   float64
 8   ODR            7560 non-null   float64
 9   ODG            7560 non-null   float64
 10  ODB            7560 non-null   float64
 11  NODR           7560 non-null   float64
 12  NODG           7560 non-null   float64
 13  NODB           7560 non-null   float64
 14  Nucls          7560 non-null   float64
 15  Segms          7560 non-null   float64
 16  Holes          7560 non-null   float64
 17  Tails          7560 non-null   float64
 18  Nucleols       7560 non-null   float64
 19  NuclDensBrd    7560 non-null   float64
 20  NuclZDens      7560 non-null   float64
 21  NuclEuFraq     7560 non-null   float64
 22  NuclEuMeanDF   7560 non-null   float64
 23  NuclEuFFDist   7560 non-null   float64
 24  NuclEuFFChain  7560 non-null   float64
 25  GrODR          7560 non-null   float64
 26  GrODG          7560 non-null   float64
 27  GrODB          7560 non-null   float64
 28  GrODH          7560 non-null   float64
 29  ODRCN          7560 non-null   float64
 30  ODGCN          7560 non-null   float64
 31  ODBCN          7560 non-null   float64
 32  GrRODR         7560 non-null   float64
 33  GrRODG         7560 non-null   float64
 34  GrRODB         7560 non-null   float64
 35  Type_real      7560 non-null   object 

dtypes: float64(35), object(1)


<br>