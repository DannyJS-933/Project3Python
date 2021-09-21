#Calcular cuanto dinero recibe cada area anualmente:
#Ginecologia: 40%, Traumatologia: 30%, Pediatria: 30%


def presupuesto():
    ginecologia = 0.40
    traumatologia = 0.30
    pediatria = 0.30
    presupuesto_total = 30000000

    presupuesto_ginecologia = presupuesto_total - ginecologia
    presupuesto_traumatologia = presupuesto_ginecologia - traumatologia
    presupuesto_pediatria = presupuesto_traumatologia - pediatria

    print(f'El presupuesto anual para Ginecologia es {presupuesto_ginecologia} \n'
          f'El presupuesto para Traumatologia es {presupuesto_traumatologia} \n'
          f'El presupuesto para Pediatria es {presupuesto_pediatria}')

presupuesto()