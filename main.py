import sys, time
import os

k = 0

def delprint(text:str="Type a string in",delay_time:int=.05): #Delayed printing function
    for character in text:      
        sys.stdout.write(character) #writes the character
        sys.stdout.flush()
        time.sleep(delay_time)#this is the delay time between each character
    print()

def ok():
    print('\nНажмите enter')
    input()
    os.system('cls')

def badEnd():
    delprint('«Да вы шпион, Шуренберг! Расстрелять на месте!»\nПослышались выстрелы. «Нет, мы стрелы» — легко парировал Шуренберг. Так и закончились дни славного разведчика, служившего на благо родины.')

delprint("Здравствуйте, Юрий Штернман. Генштаб ГРУ прислал вам новое задание:\nУже завтра, 30 марта 1945 года пройдет заседание НСДАП по делам о Западном фронте. Вы обязаны туда явиться в своем обычном репертуаре, как штандартенфюрер Ганс Шуренберг. Напомним, что неделю назад вы были произведены из оберштурмбаннфюрера, получив новую должность. По планам завтра завершится наше наступление на Данциг, а далее мы последуем на Вену. Ваша задача – запутать членов НСДАП и отсрочить реакцию германского правительства на эти события. Не забудьте о консперации, начало заседания в 10 утра.")

ok()

delprint("На следующий день...")
ok()

delprint("Шуренберг шел по улицам старого Берлина. Где-то гремели сирены, однако ему было не до этого. На нем сверкали новые погоны, на фуражке красовались череп и блестящий орёл. Он был с иголочки одет в чёрное пальто, сшитое HUGO BOSS. Петлицы напоминали всем вокруг о его новом звании. Наконец он дошел до здания:\n— Хайль Гитлер! - охранник.\n— Хайль.\n— Кто вы и по какому поводу?\n— Ганс Шуренберг, прибыл на заседание Nationalsozialistische Deutsche Arbeiteipartei.\n— Вашего имени нет в списке...\n1) Показать удостоверение разведчика\n2) «Произошла ошибка, вот приглашение, оно должно там быть!»\n3) Промолчать")

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)

if answer == 1: k -= 3
elif answer == 2: k -= 1
elif answer == 3: k += 2

ok()

delprint('Ганс поднимался по лестнице на верхний этаж, где проходит заседание...')
ok()

delprint('Вдруг, рука опускается к нему на плечо, что его и останавливает. Штраус оборачивается и видит обергруппенфюрера, начальника РСХА Эрнста Кальтенбруннера.\n— Зиг хайль *приглядывается на погоны*, штандартенфюрер. — Что-то я не видел вашего лица среди руководства СС ранее. Представьтесь, пожалуйста.\n— Ганс Шуренберг, недавно был произведен из оберштурмбаннфюрера в штандартенфюрера. Заседания НСДАП посещаю недавно, однако...\n1) ...сделаю все на славу Рейха и его победы!\n2) ...долг есть долг, и раз меня поставили на эту должность...')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)

if answer == 1: k += 1
elif answer == 2:
    delprint('1) ...буду выполнять свои обязанности\n2) ...отдам себя службе Рейху')
    answer = input()

    while answer.isdigit() == False:
        print('Введите число')
        answer = input()
            
    answer = int(answer)
    if answer == 1: k -= 1
    elif answer == 2: pass

ok()

delprint('— Прелестно, в таком случае, не расскажите ли, чему посвящено наступное собрание?\n— Конечно, мы собираемся обсуждать...\n1) Дела внутри партии\n2) Эффективность деятельности контрразведки\n3) Наступление союзников во Франции')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1 or answer == 2: k -= 1
elif answer == 3: k += 2

delprint('— Что ж, я вижу вы можете тут находиться, не смею больше вас задерживать.')

ok()

delprint('Ганс входит на заседание:\n1) — Хайль Гитлер\n2) — Рот фронт, товарищи нацисты!\n3) — Зиг хайль')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 2
elif answer == 2: k -= 2
elif answer == 3: k += 1

ok()

delprint('Он садится за стол, оглядывается по сторонам. В углу сидит Борман, Адольф Вагнер сразу за ним. Дальше, во главе стола ведёт заседание Геринг, соседствуя с Гиммлером. Совет военный, потому офицеры Вермахта собрались тут все вместе. Разведчик уже занял свое место, как вдруг замечает на полу пистолет. Первая его мысль — сообщить кому-то. Но потом он:\n1) Забрал его себе.\n2) Рассказал сидящему рядом гестаповцу.\n3) Отбросил его в угол.')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 1
elif answer == 2: k -= 2
elif answer == 3: pass

delprint('После Шуренберг посмотрел на свою кобуру и заметил, что там пусто. Оказалось, это был его пистолет.')

ok()

delprint('Заседание продолжалось. Выступал Геринг:\n— Господа, ещё недели не прошло с того, как Союзники форсировали Рейн, закрепившись предварительно на плацдармах под Ремагеном. Мы вынуждены срочно реагировать! Я предлагаю...\n\nВдруг резко распахивается дверь и вбегает оберштурмфюрер Штраус. «У меня срочный доклад!» — заявил вбежавший офицер. «Вы не видите, у нас заседание!» — рявкнул председатель. «Совершенно срочно, господин рейхсмаршал! Необходимо здесь же и сейчас рассмотреть порядок реагирования, иначе весь Восточный фронт окончательно падёт». «В таком случае, докладывайте» - умерил свой пыл наконец герр Геринг. В тот момент шпион смекнул, что наступление-таки удалось.\n\nШтраус начал свой доклад и очень быстро перешёл к главной его части:\n— <...> Сегодня утром, практически только что, в генштаб Вермахта пришла телеграмма. Данциг пал, советы завершили захват города.\n1) Промолчать\n2) Урааа! Вперёд, красноармейцы ✩\n3) Нахмурить лицо')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: pass
elif answer == 2: k -= 2
elif answer == 3: k += 2

delprint('— Однако это еще не все. Разведка доложила, что вот-вот русские начнут наступление на Вену. Все плацдармы подготовлены, а люди и техника наготове, поэтому не доверять этой информации резона не видно. Очевидно, с этим нужно что-то делать.\n— Что ж, вы правы, доклад стоил быть услышанным, — согласился Геринг, — спасибо, что настояли. Мне нужно обдумать услышанное, так как сгоряча действовать нельзя, хотя и следует что-то срочно предпринять. Пока хотелось бы услышать мнение кого-нибудь другого. Например, кого-то нового, не помешало бы услышать свежий взгляд. О, недавно же у нас появился новый штандартенфюрер. Шуренберг, если не ошибаюсь? Что вы думаете?\n1) Надо во всем разобраться.\n2) Нужно действовать сейчас же!\n3) Да здравствует Советская армия рабочих и крестьян!')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)

if answer == 2:
    delprint('— Пока советы только закончили операцию по взятию Данцига, они истощены. Пока не прибыли резервы, продовольствие и боеприпасы, надо наносить удар! В Вене у нас состредоточены войска, многие дома превращены в укреплённые опорные пункты с пулеметами и ПТО, Райхсбрюке заминирован! За нее опасаться не стоит, а вот дать русским возможность отдохнуть нельзя. Поэтому сейчас же необходимо отдать приказ о контрнаступлении на группировку советских войск.')
    k += 1

elif answer == 1:
    delprint('— Конечно, новости это плохие. Однако я считаю, что нужно взвешено принимать решения. К примеру, не забывая тему конференции, не стоит бездумно перекидывать войска с Западного фронта, ибо в таком случае тот падёт ещё быстрее, а без грамотной стратегии Восточный мы даже с подкреплением не удержим. Надо перегруппироваться у Вены, Данциг все равно уже сдан, и держать оборону до подкрепления, а потом начинать контрнаступление.')
    k += 2

elif answer == 3:
    delprint('— Не могу не радоваться успехам наших ребят. Да, в Вене будет сложно, но и она падает и будет освобождена, мы все ближе к границам, и через месяцок вы же сами в своих же бункерах закончитесь, как и ваш фюрерок. Ребятки, мне кажется надо накупить попкорну и ждать, смотреть было бы оптимальным решением.')
    k -= 2

ok()

delprint('Ганс фон Шуренберг частенько захаживал к гадалке и знал, что всего за восемь суток Вена падёт так же, как и Данциг. Немцы будут окружены с трёх сторон, отреза от путей к отступлению и в итоге их сопротивление сломится.')

ok()

delprint('— Гм, благодарю, господин штандартенфюрер. Интересно было услышать вашу точку зрения. Ну, я думаю, дела Западного фронта могут подождать на фоне таких новостей, поэтому объявляю временный перерыв. Через час собираемся тут же ещё раз и обсуждаем сначала вопрос с советами, а потом и с Союзниками, так как мне нужно посоветоваться с фюрером.\n\nНа этом моменте послышались звуки. В дверь постучали 8 раз. «Осьминог» — подумал Шуренберг. «8 нацистов» — легко парировал Миллер, его воображаемый друг. Это были опоздавшие офицеры, у которых была депрессия и рассеянность на фоне неудач. «Опять эти новобранцы недобросовестно выполняют свои обязанности нацистов! Куда смотрят инструкторы разведки..." - бормотал про себя Ганс.\n1) «Освобожусь, устрою им хорошую взбучку»\n2) «Похвалю за то, что порочат образ нацистов»\n3) «Эх, разгильдяи, но это дело ГРУ, ничего не буду делать»')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 1
elif answer == 2: k -= 1
elif answer == 3: pass

delprint('— добавил в мыслях разведчик.')
ok()

delprint("Но в заседании был перерыв, и Шуренберг освободился. Он решил прогуляться по душным коридорам Гестапо. Тяжесть гнетущего нацизма и тоски по родине давили на него, но Юрий выдерживал все испытания, психологические не были исключением. «Пыточная, переговорная, пыточная, зал заседаний, пыточная... столовая!» - перечислял про себя Шуренберг, проходя все новые двери. Но вот он добрался до столовой. За витриной уже стояла Герда, что была готова обслужить нацистов. Ходили слухи, что имя ей досталось после перечисления ее польским прадедом случайных женских имён: «Марта, Цецилия, Берта... Герда!». Наконец Шуренберг промолвил:\n1) — А налей-ка борщецу, смачного, как баба Маша на Украине делала! И водочки, Столичной...\n2) — Мне, пожалуйста, швепс и Bauernfrühstück\n3) — Здравствуйте, добавьте в заказ БигМак, наггетсы 9 штук и большую колу. Спасибо.")

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k -= 2
elif answer == 2: k += 2
elif answer == 3: pass

ok()

delprint('Ганс получил свою еду и отправился к своим товарищам-нацистам за стол. Они обсуждали насущные вопросы, как сыграл гамбургский Гамбург и баварская Бавария. Два однокашника (поговаривают, в те времена нацисты очень любили кашу) Шуренберга болели за разные команды, а матч закончился вничью, потому и пытались решить, а кто же всё-таки сыграл лучше. Спор ни к чему не привел, потому решили спросить Ганса:\n— Как, по-твоему, кто же всё-таки сыграл лучше?\n1) — «Гамбург» долго доминировал в гаулиге Нордмарк, там собраны одни профессионалы! Конечно, «Бавария» показала себя достойно, даже сыграв с ничейным счётом, но, конечно, с мастерством игры гамбургцев никто не сравнится.\n2) — «Бавария» долго время хорошо себя показывала, в 1932 году даже триумфально обыграв «Айнтрахт». Единственная причина, почему они перестали быть такими результативными, — Гестапо, что начали охоту на их президента и тренера, из-за которой им обоим пришлось покинуть Рейх. Но команда показала себя достойно и имела все шансы обыграть Гамбург. Они, конечно, сыграли лучше!\n3) — Ребят, ну какой это вопрос. Московское Динамо, естественно, сыграло лучше всех. Яшин, к сожалению, за них пока не играет, но величие клуба это не отменяет, а он ещё покажет блестящую победу советов на Олимпиаде. Так что, без обсуждений, конечно это были сине-бело-голубые.')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 1
elif answer == 2: k -= 1
elif answer == 3: k -= 2

delprint('Собеседники услышали мнение Шуренберга и поспешили удалиться. «Испугались настоящего футбольного гуру» — подумал Шуренберг.')
ok()


delprint('Оставшись в одиначестве, разведчик доел еду и поспешил выйти. До продолжения заседания ещё оставалось время. Шуренберг решил скоротать его, покурив папиросу, что с Кубы привез ему его дядя (вскоре из-за ломки по ним ее придется заманить в лоно Советского Союза, дабы избавиться от пошлин: больно дорогие - 10 рейхсмарок 50 рейхспфеннингов!). Однако курилка находилась этажом выше. Пока Шуренберг поднимался по лестнице, он увидел, как двое иммигрантов с юга - итальянцы - вешали на стену портрет Фюрера кисти самого Гайзенберга. На что Шуренберг:\n1) Промолчал.\n2) «Вешайте-вешайте, господа итальяшки. Муссолини уже сам висит, как и скоро будет и сам Гитлер. Пока наши бравые воины подходят к Вене, этот, должно быть, в своем бункере рвет на себе волосы, не понимая, как отсталая страна, где абсолютно нелегитимное правительство, смогла дать вам такой отпор, так ещё и побеждает. Удачки)»\n3) «Хайль Гитлер»')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: pass
elif answer == 2: delprint('Xорошо, что необразованные итальянцы не понимают русский, в отличие от остальных высокопоставленных нацистов. Поэтому это ни на что не повлияло.')
elif answer == 3:
    delprint('"Ave Caesar" - послышалось в ответ.')
    k += 1

delprint('Разведчик продолжил дальше свой путь.')
ok()

delprint('Пока Шуренберг шел, его одалела тоска по родине. Где он мог спокойно прогуляться по родным улочкам, говоря на своем родном идише, а не напрягаться, играя русского разведчика.\n1) «Сорваться бы, купить билетов и на юг, в Анапу! Вот уже 9 мая на носу, надо бы подготовиться...»\n2) «Нацистом быть не так уж и плохо, жаль только льготного проезда нет, а в целом кормят хорошо, да и форма удобная».\n3) «Зиг-зиг хайль зиг хайль, зиг-зиг-зигушки хайлюшеньки».')
input()
delprint('— думал про себя разведчик.')
ok()

delprint('Наконец он дошел до двери курилки. На ней висела табличка "не петь". Шуренберг удивился, ведь агента Петю центр отозвал ещё месяц назад. Он отворил die Tür и вошел в узкий и насквозь порочный круг нацистских курильщиков. Его встретили Гёхлер, Зинберг, Бицманн и Меллингхер. «Ayo wasaaap» — подумал Шуренберг. И пятеро друзей дружно затянулись. Ой благодать пошла!.. Шуренберга потянуло на стихи:\n1)\nDeutschland! Mein Herz in Flammen\nWill dich lieben und verdammen\nDeutschland! Dein Atem kalt\nSo jung und doch so alt\n2)\nЯ\n достаю\n     из широких штанин\nдубликатом\n      бесценного груза.\nЧитайте,\n     завидуйте,\n           я —\n             гражданин\nСоветского Союза.\n3)\nОй пошел наш Шуренберг\nПогулять по улице!\nВсе - что немки, что Вайсберг\nПо улыбке на лицах!\n\nА когда заговорил\nНаш разведчик бравый,\nТак и выпал крокодил\nПоедавший травы!')


answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 2
elif answer == 2: k -= 2
elif answer == 3: k -= 1

delprint('На что Отто спросил Ганса:\n— Послушай, Гансик. Ну уже во всем гестапо тебя считают советским шпионом! Что ж ты такое делаешь, чтоб себе такую репутацию заработать?\n1) — Понимаешь, я же штандартенфюрер СС, очень желанная цель для ГРУ ГШ ВС СССР. Их разведка тоже не дремлет, вот агенты и пытаются очернить мое доброе арийское имя. А олухи из тайной полиции на се ведутся, эх, с каждым бы поговорил!\n2)\n איזה סובייטי?! אני מייצג רק את האינטרסים של ישראל —\n3) — Понимаешь, дело в том, что я и есть шпион. Ну надоело скрываться, на-до-е-ло! А никто не может на меня ничего найти! Даже Миллер, сколько бы ни хлопотал, все не может. Так что к чему боле конспирация ¯⁠\⁠_⁠(⁠ツ⁠)⁠_⁠/⁠¯')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 1
elif answer == 2 or answer == 2: k -= 2

delprint('Зинберга удовлетворил ответ Ганса. А Шуренберга — нет. «Это при условии, что х ≠ ±√3»— дополнил разведчик.')

ok()

delprint('Шуренберг решил разрядить обстановку. Штаб настаивал на том, что у немцев неплохое чувство юмора, поэтому разведчик решил зайти с анекдотов про Штирлица:\n1) — Штирлиц стрелял вслепую. Слепая испугалась и побежала скачками, но качки быстро отстали.\n2) — Подвыпившие Штирлиц и Мюллер вышли из бара.\n- Давайте снимем девочек, - предложил Штирлиц.\n- У вас очень доброе сердце - ответил Мюллер. - Но пусть все-таки повисят до утра.\n3) — Штирлиц стоял на своем. Это была любимая пытка Мюллера.')

input()

delprint('«Ахахахах» — прыснул Отто. Обстановка была разряжена — цель достигнута. Шуренберг докурил папироску и удалился.')

ok()

delprint('Пока оставалось немного времени до продолжения совещания, Шуренберг решил сделать кружок по дневному Берлину. Архитектура Фридрихштадта поражала, а весна уже вовсю разыгрывалась. Вильгельмштрассе снова сотрясалась от взрывов бомб и артиллерии, однако Шуренберг не пугался: пилоты и наводчики знали его в лицо и обещали бить не в него. По дороге Ганс встретил своего товарища по службе - Макса Гегенфойлера. У них завязался разговор, пока они шли по пыльным тратуарам погрязших в нацистском блуде улиц.\n— А знаешь, Ганс, мой дед как-то сказал: «какой шпион не русский». Так что, получается, раз ты шпион, то работаешь на советов? — с довольной ухмылкой победителя спросил Оберштурмбаннфюрер.\n— Послушай, Максимка, — молвил разведчик, — ты перед тем, как предателем родины кликать, улики поднул? — поднял бровь (+_-) Ганс.\n— Прямых улик, к сожалению, нет( — грустно ответил Гегенфойлер.\n— Тогда работай лучше! Ну ведь голимый шпион перед тобой, ты ещё и общаешься тесно, а так до сих пор и не раскусил... Да... каких шпионов в Союзе делают, школу не проколбасишь! — чуть не сорвался Шуренберг.\n— До тех пор, пожалуй, продолжу работать...\n1) ...на Рейх.\n2) ...штандартенфюрером.\n3) ...русским шпионом.')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1 or answer == 2: k += 1
elif answer == 3: k -= 1

delprint('— наконец ответил разведчик.')

ok()

delprint('Но вот время подходит к совещанию. Огни снарядов освещали пасмурное небо столицы Рейха. Наконец он дошел до улочки, что вела прямиком к дворцу принца Альбрехта, штаб квартире Гестапо.\n— Вы появились, штандартенфюрер! — сказал охранник, — Проходите.\n1) — Эти немцы, все им точно надо! Вот у нас в России можно нормально приходить с опозданием и без лишней ругани. Самая сложная вещь в моей работе шпиона!\n2) — Ещё раз здравствуйте, герр Sicherheitsbeamter.\n3) — Зиг хайль!')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k -= 2
elif answer == 2: k += 1
elif answer == 3: k += 2

delprint('— ответил Шуренберг. Он вошёл в здание.')

ok()

delprint('Уже по дороге к месту заседания, его окликнул гауптштурмфюрер. Он пригласил его в кабинет Бергмана. Тот хотел дать ему задание. «За свое дание никому не позволю дать!» — думал про себя разведчик Шуренберг. Он отворил дверь. За своим столом сидел группенфюрер. Три дубовых листа со звездой красовались на петлицах.\n— А вот и вы, господин Шуренберг! — воскликнул Хельмут. — По вашему произведению в штандартенфюреры у меня для вас новое задание: вы должны стать двойным агентом в СССР в нашу пользу. Эта миссия — последняя надежда для Рейха.\n1) — Понимаете, я бы с радостью! Да вот семья, дети - не могу. Рад бы!.. да не могу, прошу прощения...\n2) — Да как же я, ещё и за своей страной шпионить! Конечно, двойной агент и все такое, но вдруг я случайно хотя бы одному человеку жизнь погублю — Я на такое пойти не могу. Делайте что хотите, а я согласиться не могу.')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k += 1
elif answer == 2: k -= 2

delprint('— Как же я от вас всех устал, — вымолвил Бергман. Вдруг за окном что-то грохнулась на брусчатку. Это был Бергман. «Третий раз за день принимаем» — крикнул выглянувшему Шуренбергу нацист с простыней в руках.\n1) — Эх, не бережете вы себя, нацистики мои! Кого ж мы вешать будем, когда победим? Вы аккуратнее...\n2) — Экая оказия! Осторожнее, гауптштурмфюрер, не пораньтесь. Голову потом тяжело лечить будет!..')

answer = input()

while answer.isdigit() == False:
    print('Введите число')
    answer = input()
        
answer = int(answer)
if answer == 1: k -= 2
elif answer == 2: k += 1

ok()

delprint('Шуренберг выдохнул. «Минус один» — подумал разведчик. «Вообще-то, тут 3¼»— ловко поправил его по нацистский математик, переворачивая доску. Разведчик продолжил движение к начинающемуся заседанию.')

ok()

delprint('За минуту до начала Шуренберг влетает в зал. Там уже все собрались. Вдруг один из сидевших спиной к разведчику разворачивается. Это был сам фюрер. Шуренберг:\n1) Ахнул\n2) Охнул\n3) Ухнул')

input()

delprint('На что раздался Его глас:')

if k >= 16:
    delprint('— О, это вы, штандартенфюрер Шуренберг! За ваш неоценимый вклад в азвитие Рейха вам назначено дополнительное жалование. Пожалуйста, присоединяйтесь.\n\nЗаседание продолжалось спокойно, а разведчик и дальше день за днём приближал победу своего отечества...')
if k <= -19:
    badEnd()
else:
    delprint('— Знаете, господин Шуренберг, вы подозреваетесь в шпионаже. Что вы скажете в свое оправдание?\n1) — Как я могу быть шпионом, если я разведчик?!\n2) — Вы можете подозревать меня в чем хотите, однако я навсегда останусь верен Рейху.')
    
    answer = input()

    while answer.isdigit() == False:
        print('Введите число')
        answer = input()
            
    answer = int(answer)
    if answer == 1: badEnd()
    else: delprint('Вы правы, вам не о чем волноваться, мне была интересна ваша реакция. Что ж, продолжим заседание.')

ok()

delprint('The end')

ok()

delprint('Оцените игру (сами для себя, хотя можете и передать разработчикам):\nСценарий\nГеймплей\nЗадумка')

ok()

delprint('Титры:\nАвтор задумки, автор сценария, звукорежиссёр, постановщик сцен, художник по костюмам, CGI-директор, актер озвучки, продюсер, начальник операторской команды, главный и единственный разработчик:\nРепьев Петр\n\nОтдельная благодарность:\nПольскому прадеду за помощь в развитии отдельных деталей сюжета\n\nБолгарской бабушке за поддержку походу разработки\n\nУзбекскому дяде, благодаря которому разработчики обладали необходимыми для разработки знаниями')

ok()

delprint('Гитлер капут!')

ok()

# 24 is max k up to that moment

print(f'Ваш счет - {k} баллов')
