from sklearn import datasets
from sklearn import model_selection
import pandas as pd

def zad1():
    x = datasets.load_wine()
    print("Dane o winach: ", x)

def zad2():
    x = datasets.load_wine(as_frame="true")
    X_train, X_test, y_train, y_test = model_selection.train_test_split(x.data,x.target,test_size=0.4)
    print("X test: ", X_test)
    print("-------------------")
    print("X train: ", X_train)
    print("-------------------")
    print("Y test: ", y_test)
    print("-------------------")
    print("Y train: ", y_train)
    print("-------------------")
    pd.DataFrame.to_csv(X_test, 'out/X_test.csv')
    pd.DataFrame.to_csv(X_train, 'out/X_train.csv')
    pd.DataFrame.to_csv(y_test, 'out/y_test.csv')
    pd.DataFrame.to_csv(y_train, 'out/y_train.csv')

def zad3_analyse(dataset):
    pd.DataFrame = dataset
    valueCount = pd.DataFrame.size
    uniqueValueCount = pd.DataFrame.nunique()
    meanValue = pd.DataFrame.mean()
    numberOfNulls = pd.DataFrame.isna().sum()
    maxValue = pd.DataFrame.max()
    minValue = pd.DataFrame.min()
    commonValue = pd.DataFrame.mode()
    print("Ilosc wartosci: ", valueCount)
    print("--------------------")
    print("Ilosc wartosci unikatowych: ", uniqueValueCount)
    print("--------------------")
    print("Wartosc srednia w zbiorze: ", meanValue)
    print("--------------------")
    print("Ilosc wartosci null: ", numberOfNulls)
    print("--------------------")
    print("Wartosc maksymalna: ", maxValue)
    print("--------------------")
    print("Wartosc minimalna: ", minValue)
    print("--------------------")
    print("Wartosc najczesciej wystepujaca w zbiorze: ", commonValue)
    print("********************")


def zad3():
    X_train = pd.read_csv('out/X_train.csv')
    y_train = pd.read_csv('out/y_train.csv')
    X_test = pd.read_csv('out/X_test.csv')
    y_test = pd.read_csv('out/y_test.csv')
    zad3_analyse(X_train)
    zad3_analyse(y_train)
    zad3_analyse(X_test)
    zad3_analyse(y_test)

zad3()