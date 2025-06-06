# Tools do projeto

def acarv(gastos_mes: float, hd_essencial: int, dm_essencial: int, custos_projeto: float, 
            hd_operacional: int, dm_operacional: int, margem: int):
  """
  Função para calcular o método acarv, que foi desenvolvido pela Ana Carvalho RP, no LinkedIn. Esse método consiste em 
  verificar qual é a hora_boleto, ou seja, quanto a pessoa precisa ganhar por hora para cobrir os custos essenciais. 
  Também calcula a hora_projeto, que corresponde a quanto a pessoa usuária precisa ganhar por hora para 
  cobrir os custos operacionais. Por fim, devolve o valor total que deve ser informado como orçamento
  para realizar o projeto.
  """
  hora_boleto = gastos_mes / (hd_essencial * dm_essencial)
  hora_projeto = custos_projeto / (hd_operacional * dm_operacional)
  hora_trabalho = hora_boleto + hora_projeto
  valor_total = (hora_trabalho * (hd_operacional * dm_operacional)) * (1 + (margem/100))
  return round(valor_total, 2)
  

