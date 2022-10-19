class ReajusteSalarial:
  def __init__(self, salario, reajuste):
    self.salario = salario
    self.reajuste = reajuste

  def get_salario(self):
    return self.salario

  def set_salario(self, salario):
    self.salario = salario

  def get_reajuste(self):
    return self.reajuste

  def set_reajuste(self, reajuste):
    self.reajuste = reajuste

  def mostrar_salario(self):
    print(f"O valor do salario inicial:{self.salario}")

  def mostrar_reajuste(self):
     print(f"O valor do salario inicial:{self.reajuste}")

  def calcular_reajuste(self):
    if self.get_salario() <= 280 and self.get_reajuste() == 0.20:
      valor_reajuste = (self.get_salario() * self.get_reajuste()) + self.get_salario()
      print(f"O valor do novo salario:{valor_reajuste}")
    elif self.get_salario() >= 280 and self.get_salario() <= 700 and self.get_reajuste() == 0.15:
      valor_reajuste = (self.get_salario() * self.get_reajuste()) + self.get_salario()
      print(f"O valor do novo salario:{valor_reajuste}")
    elif self.get_salario() >= 700 and self.get_salario() <= 1500 and self.get_reajuste() == 0.10:
      valor_reajuste = (self.get_salario() * self.get_reajuste()) + self.get_salario()
      print(f"O valor do novo salario:{valor_reajuste}")
    elif self.get_salario() >= 1500 and self.get_reajuste() == 0.05:
      valor_reajuste = (self.get_salario() * self.get_reajuste()) + self.get_salario()
      print(f"O valor do novo salario:{valor_reajuste}")
    else:
      print(" verifique se o reajuste ou salario esta correto!")
    
  def mostrar_aumento(self):
    if self.get_salario() <= 280 and self.get_reajuste() == 0.20:
      valor_aumento = self.get_salario() * self.get_reajuste()
      print(f"O valor do novo salario:{valor_aumento}")
    elif self.get_salario() >= 280 and self.get_salario() <= 700 and self.get_reajuste() == 0.15:
      valor_aumento = self.get_salario() * self.get_reajuste()
      print(f"O valor do novo salario:{valor_aumento}")
    elif self.get_salario() >= 700 and self.get_salario() <= 1500 and self.get_reajuste() == 0.10:
      valor_aumento = self.get_salario() * self.get_reajuste()
      print(f"O valor do novo salario:{valor_aumento}")
    elif self.get_salario() >= 1500 and self.get_reajuste() == 0.05:
      valor_aumento = self.get_salario() * self.get_reajuste()
      print(f"O valor do novo salario:{valor_aumento}")
    else:
      print("verifique se o reajuste ou salario esta correto!")

