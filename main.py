from  config import *
from  functions import *

data = pd.read_csv(csv_file)

# show data information
print(data.head())
print(data.info())
print(data.describe())
print(data['Type_real'].value_counts())

## Исследовательскй анализ

#Построим графики распределения для всех столбцов и отобразим выбросы. При наличие в столбцах аномальных значений исправим данные значения.

for i in data.select_dtypes(exclude='object'):
    graph(data, i, i, i)

#Анамальные данные были выявлены в столбцах

#NCCave , ODB, NODB, Gr RODB,

#CArea NFFact, NODG, NODR, Granuls, GRodh, ODBcn

#Рассмотрим данные столбцы подробней
#*********************************************
#Столбец NCCave
data = remove_outliers(data, 'NCCave', 1.5)

#Столбец ODB
data = remove_outliers(data, 'ODB', 0.6)

#Столбец NODB
data = remove_outliers(data, 'NODB', 0.75)

#Столбец GrRODB
data = remove_outliers(data, 'GrRODB', 40)

#Столбец CArea
data = remove_outliers(data, 'CArea', 800)

#Столбец NFFact
data = remove_outliers(data, 'NFFact', 55)

#Столбец NODG
data = remove_outliers(data, 'NODG', 2.5)

#Столбец GrODH
data = remove_outliers(data, 'GrODH', 150)


#Столбец ODBCN
data = remove_outliers(data, 'ODBCN', 1.5)

data = data.reset_index(drop=True)

print(data.info())

#проверим данные на мультиколлинеарность
plt.figure(figsize=(20,22))
sns.heatmap(data.drop('Type_real',axis=1).corr(method='spearman'), cmap="YlGnBu", annot=True)
plt.show()

#Столбцы

#NFFact -NCCave

#NArea- NuclEuFFDist

#NuclEuFFChane - NuclEuFFDist

#GrRODR - GrRODG

#Удалим столбцы с высокой кореляции

data = data.drop(['NCCave','NuclEuFFDist','GrRODG', 'NuclEuFFChain'], axis=1)

plt.figure(figsize=(20,22))
sns.heatmap(data.drop('Type_real',axis=1).corr(method='spearman'), cmap="YlGnBu", annot=True)
plt.show()


# Разделим данные

x = data.drop('Type_real', axis=1)
y = data['Type_real']

x_train, x_test ,y_train ,y_test  = train_test_split(x,y, test_size=0.2)

# создайте экземпляр класса LabelEncoder для кодирования целевого признака
label_encoder =  LabelEncoder()

# обучите модель и трансформируйте тренировочную выборку
target_train = label_encoder.fit_transform(y_train)


# трансформируем тестовую выборку
target_test = label_encoder.transform(y_test)
#Создадим пайплайн для масштабирования целевого призныка (и если буедт необходимо заполнение пропусков)
prepare_data = Pipeline([
    ('simpleImp', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
    ('scaler', StandardScaler() )
])

#Создадим датафреймы с машстабированными призныками

feature_train = pd.DataFrame(data = prepare_data.fit_transform(x_train),
                       columns=prepare_data['scaler'].get_feature_names_out())
feature_test = pd.DataFrame(data = prepare_data.transform(x_test),
                       columns=prepare_data['scaler'].get_feature_names_out())

#Инициализируем и обучис модель RandomForestClassifier
rfc=RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators': [200, 500],
    'max_depth' : [4,10,20 ],
}

CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 3, verbose=True)

CV_rfc.fit(feature_train, target_train)
print('RandomForestClassifier best estimator', CV_rfc.best_estimator_)

pred_rfr = CV_rfc.predict(feature_test)

print_results(target_test, pred_rfr, label_encoder)


#Обучим классификатор CatBoostClassifier
parameters = {'depth'         : [4, 10, 20],
              'iterations'    : [10,50, 100]
             }

CBC = CatBoostClassifier()

Grid_CBC = GridSearchCV(estimator=CBC,
                        param_grid = parameters,
                        cv = 3)

Grid_CBC.fit(feature_train, target_train)

print('CatBoostClassifier best estimator', Grid_CBC.best_estimator_)

pred_cbc = Grid_CBC.predict(feature_test)



print_results(target_test, pred_cbc, label_encoder)
