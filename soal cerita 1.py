bebek_jantan = 63
bebek_betina = 192

bebek_betina = bebek_betina + bebek_jantan
bebek_jantan = bebek_jantan - (bebek_jantan// 3)


bebek_jantan = bebek_jantan + bebek_betina
bebek_betina = bebek_betina - 10


total = bebek_betina + bebek_jantan
print(total)