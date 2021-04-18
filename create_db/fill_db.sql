
INSERT INTO ogranizations (title, inn, created_at, udated_at)
VALUES 
	('Центр управления проектами ООО', 74488, DATETIME('now', 'localtime'), DATETIME('now', 'localtime')),
	('Новые горизонты ООО', 7548, DATETIME('now', 'localtime'), DATETIME('now', 'localtime'));


INSERT INTO contractors (title, inn, created_at)
VALUES
	('Дроб-Сервис ООО', 8364028, DATETIME('now', 'localtime')),
	('Башенные краны ООО', 093487, DATETIME('now', 'localtime')),
	('Нерудные материалы ООО', 98763, DATETIME('now', 'localtime')),
	('Грузоподъемная техника ООО', 67537613, DATETIME('now', 'localtime')),
	('Трактора и трактористы ООО', 8374322, DATETIME('now', 'localtime')),
	('Какие-то экскаваторы ООО', 8763487, DATETIME('now', 'localtime')),
	('Бетононасосы и миксера ООО', 9748932, DATETIME('now', 'localtime')),
	('Самосвалы Урала ООО', 32451435, DATETIME('now', 'localtime'));
	
-- DELETE FROM contractors;


INSERT INTO builders (title, inn, created_at)
VALUES
	('ЮжУралСтрой ООО', 9845792, DATETIME('now', 'localtime')),
	('Отделочные работы в строительстве ООО', 9274942, DATETIME('now', 'localtime')),
	('Кирпичное домостроение ООО', 9827371, DATETIME('now', 'localtime')),
	('Фасады и окна ООО', 3452573, DATETIME('now', 'localtime')),
	('Стройком СК ООО', 983272, DATETIME('now', 'localtime')),
	('Сантехника на века ООО', 736784, DATETIME('now', 'localtime'));

-- DELETE FROM builders;

INSERT INTO projects (title, organization_id, created_at)
VALUES
	('жд 34/34', 1, DATETIME('now', 'localtime')),
	('жд 30/34', 1, DATETIME('now', 'localtime')),
	('жд 15/33', 1, DATETIME('now', 'localtime')),
	('Автопарковка 40/34', 1, DATETIME('now', 'localtime')),
	('м-н 23/Манхеттен', 2, DATETIME('now', 'localtime')),
	('жд 3/Манхеттен', 2, DATETIME('now', 'localtime')),
	('жд 5/Мнахеттен', 2, DATETIME('now', 'localtime')),
	('жд 7/Манхеттен', 2, DATETIME('now', 'localtime'));


INSERT INTO workpacks (title, created_at)
VALUES
	('Подготовительные работы', DATETIME('now', 'localtime')),
	('Земляные работы', DATETIME('now', 'localtime')),
	('Фундаменты', DATETIME('now', 'localtime')),
	('Конструкции сборные железобетонные', DATETIME('now', 'localtime')),
	('Отделочные работы', DATETIME('now', 'localtime')),
	('Кровельные работы', DATETIME('now', 'localtime')),
	('Сантехмонтажные работы', DATETIME('now', 'localtime'));
	

INSERT INTO contracts (title, project_id, organization_id, contractor_id, from_date, created_at)
VALUES
	('1/125-2014/НГ', 5, 2, 38, DATE('2014-04-18'), DATETIME('now', 'localtime')),
	('3/127-2015/ЦУП', 1, 1, 42, DATE('2015-01-10'), DATETIME('now', 'localtime')),
	('17/003-2017/ЦУП', 3, 1, 39, DATE('2013-06-11'), DATETIME('now', 'localtime')),
	('125/125-2014/НГ', 7, 2, 45, DATE('2014-07-23'), DATETIME('now', 'localtime')),
	('2/009-2015/ЦУП', 2, 1, 40, DATE('2015-09-01'), DATETIME('now', 'localtime')),
	('17/123-2015/ЦУП', 4, 1, 41, DATE('2015-11-13'), DATETIME('now', 'localtime')),
	('115/008-2020/НГ', 6, 2, 43, DATE('2020-05-03'), DATETIME('now', 'localtime')),
	('25/003-2021/НГ', 8, 2, 44, DATE('2013-06-11'), DATETIME('now', 'localtime')),
	('11/125-2014/ЦУП', 1, 1, 45, DATE('2014-04-28'), DATETIME('now', 'localtime')),
	('30/127-2015/НГ', 5, 2, 39, DATE('2015-10-01'), DATETIME('now', 'localtime')),
	('117/003-2017/НГ', 6, 2, 40, DATE('2013-06-12'), DATETIME('now', 'localtime')),
	('12/125-2014/ЦУП', 2, 1, 41, DATE('2014-08-24'), DATETIME('now', 'localtime')),
	('20/009-2015/НГ', 3, 2, 38, DATE('2015-12-10'), DATETIME('now', 'localtime')),
	('170/123-2015/НГ', 7, 2, 42, DATE('2015-01-13'), DATETIME('now', 'localtime')),
	('11/008-2020/ЦУП', 4, 1, 43, DATE('2020-07-13'), DATETIME('now', 'localtime')),
	('251/003-2021/ЦУП', 8, 1, 44, DATE('2021-06-21'), DATETIME('now', 'localtime'));


-- DELETE FROM contracts;


INSERT INTO specs (title, contract_id, workpack_id, amount)
VALUES
	('1', 17, 1, 1000.25),
	('21', 18, 1, 250000),
	('3', 19, 2, 342000),
	('5', 20, 2, 115000),
	('7', 21, 3, 1864213),
	('17', 22, 3, 37488),
	('14', 23, 4, 8243),
	('326', 24, 4, 723676),
	('245', 25, 5, 3761),
	('113', 26, 5, 87126),
	('35', 27, 6, 376193),
	('34', 28, 6, 3879192),
	('24', 29, 7, 100000),
	('123', 30, 7, 1354200),
	('12', 31, 1, 1133311),
	('4', 32, 2, 200000);


INSERT INTO types (title)
VALUES
	('Башенные краны'),
	('Бульдозеры и экскаваторы'),
	('Автокраны'),
	('Фронтальные погрузчики'),
	('Телескопические погрузчики'),
	('Самосвалы'),
	('Автобетононасосы'),
	('Миксера'),
	('Полуприцепы');


INSERT INTO services (title, type_id, created_at)
VALUES
	('CGC___ Услуги погрузчика фронатльного с объемом ковша 1.0 м3', 4, DATETIME('now', 'localtime')),
	('CGC___ Услуги погрузчика фронатльного с объемом ковша 1.4 м3', 4, DATETIME('now', 'localtime')),
	('CGC___ Услуги погрузчика телескопического грузоподъемностью 3.5т', 5, DATETIME('now', 'localtime')),
	('CGC___ Услуги погрузчика телескопического грузоподъемностью 5т', 5, DATETIME('now', 'localtime')),
	('CGC___ Услуги погрузчика телескопического грузоподъемностью 10т', 5, DATETIME('now', 'localtime')),
	('CGC___ Услуги бульдозера мощностью 180 л.с.', 2,  DATETIME('now', 'localtime')),
	('CGC___ Услуги бульдозера мощностью 320 л.с.', 2,  DATETIME('now', 'localtime')),
	('CGC___ Услуги экскаватора с объемом ковша 0.4м3', 2,  DATETIME('now', 'localtime')),
	('CGC___ Услуги экскаватора с объемом ковша 1м3', 2,  DATETIME('now', 'localtime')),
	('CGC___ Услуги экскаватора с объемом ковша 1,4м3', 2,  DATETIME('now', 'localtime')),
	('CGC___ Услуги автокрана г/п 25т', 3, DATETIME('now', 'localtime')),
	('CGC___ Услуги автокрана г/п 40т', 3, DATETIME('now', 'localtime')),
	('CGC___ Услуги автокрана г/п 75т', 3, DATETIME('now', 'localtime')),
	('CGC___ Услуги башенного крана г/п 8т', 1, DATETIME('now', 'localtime')),
	('CGC___ Услуги самосвалов г/п 10т', 6, DATETIME('now', 'localtime')),
	('CGC___ Услуги самосвалов г/п 16т', 6, DATETIME('now', 'localtime')),
	('CGC___ Услуги самосвалов г/п 24т', 6, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБН с вылетом стрелы 36м', 7, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБН с вылетом стрелы 40м', 7, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБН с вылетом стрелы 52м', 7, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБС объемом 3м3', 8, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБС объемом 6м3', 8, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБС объемом 9м3', 8, DATETIME('now', 'localtime')),
	('CGC___ Услуги АБС объемом 12м3', 8, DATETIME('now', 'localtime')),
	('CGC___ Услуги полуприцепов бортовых г/п 20т', 9,  DATETIME('now', 'localtime'));
	
	
	
	








































	