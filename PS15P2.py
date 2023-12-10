class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price
      self.discount_price = 0.9 * sticker_price

  def display_details(self):
      print(f"Make: {self.make}, Model: {self.model}")
      print(f"Sticker Price: ${self.sticker_price}")
      print(f"Discount Price: ${self.discount_price}")

  def updated_price(self):
      return self.discount_price


class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.sport_wheels_option = False
      self.sport_engine_option = False
      self.sport_interior_option = False

  def add_sport_wheels(self):
      self.sport_wheels_option = True

  def add_sport_engine(self):
      self.sport_engine_option = True

  def add_sport_interior(self):
      self.sport_interior_option = True

  def pricewithoptions(self):
      price = self.updated_price()
      if self.sport_wheels_option:
          price += 1000.00
      if self.sport_engine_option:
          price += 3000.00
      if self.sport_interior_option:
          price += 2000.00
      return price



sport_car = Sport("Toyota", "Camry", 25000)


sport_car.display_details()


sport_car.add_sport_wheels()
sport_car.add_sport_engine()
sport_car.add_sport_interior()


print(f"Pricewithoptions: ${sport_car.pricewithoptions()}")
