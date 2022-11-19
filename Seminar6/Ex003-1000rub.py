#Задача 3. Имеется 1000 рублей. Бык стоит – 100
# рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все
# эти деньги, если всего надо купить 100 голов
# скота?

bullPrice = 100
cowPrice = 50
calfPrice = 5
money = 1000

for bullCount in range(money//bullPrice):
    for cowCount in range(money//cowPrice):
        for calfCount in range(money//calfPrice):
            if bullCount+cowCount+calfCount == 100 and bullCount * bullPrice + cowCount * cowPrice + calfCount*calfPrice == 1000:
                print(f'быки {bullCount}, коровы {cowCount}, телята {calfCount}') # перебрали все возможные варианты




