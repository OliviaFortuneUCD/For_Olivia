car_units = units_sold.melt(id_vars=["Make"],var_name="Date",
        value_name="units_sold")

adspend = car_adspend.melt(id_vars=["Make"],var_name="Date",
        value_name="adspend")

car_units = units_sold.melt(id_vars=["Make"],var_name="Date",
        value_name="units_sold")
adspend = car_adspend.melt(id_vars=["Make"],var_name="Date",
        value_name="adspend")

units_adspend = pd.merge(adspend, car_units, on=["Date", "Make"])