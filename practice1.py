import pandas as pd

units_sold = pd.read_csv('Car Units sold by month 2018-2021.csv')
car_adspend = pd.read_csv('Car adspend.csv')

car_units = units_sold.melt(id_vars=["Make"],var_name="Date",
        value_name="units_sold")
adspend = car_adspend.melt(id_vars=["Make"],var_name="Date",
        value_name="adspend")
if __name__ == "__main__":
    print(units_sold.info())
    print(car_adspend.info())
    print(units_sold.head())
    print(car_adspend.head())
    print(car_units.head())
    print(adspend.head())

    print(adspend.info())