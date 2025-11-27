INSERT INTO cars 
    (driver_id, mark, model, car_number, class) 
VALUES
    ((SELECT id FROM users WHERE login = 'ssmirnov'),   'Toyota',     'Camry',     'AA0001BB', 'comfort'),
    ((SELECT id FROM users WHERE login = 'mverbitskii'),'Hyundai',    'Elantra',   'AA0002BB', 'standard'),
    ((SELECT id FROM users WHERE login = 'nagent'),     'Kia',        'Rio',       'AA0003BB', 'standard'),
    (NULL,                                              'Ford',       'Focus',     'AA0004BB', 'standard'),
    (NULL,                                              'Volkswagen', 'Polo',      'AA0005BB', 'comfort'),
    (NULL,                                              'Mercedes',   'E200',      'AA0006BB', 'business'),
    (NULL,                                              'BMW',        '3 Series',  'AA0007BB', 'business'),
    (NULL,                                              'Skoda',      'Octavia',   'AA0008BB', 'standard'),
    (NULL,                                              'Renault',    'Logan',     'AA0009BB', 'standard'),
    (NULL,                                              'Nissan',     'Qashqai',   'AA0010BB', 'comfort'),
    (NULL,                                              'Honda',      'Civic',     'AA0011BB', 'standard'),
    (NULL,                                              'Chevrolet',  'Cruze',     'AA0012BB', 'standard'),
    (NULL,                                              'Opel',       'Astra',     'AA0013BB', 'standard'),
    (NULL,                                              'Mazda',      '6',         'AA0014BB', 'comfort'),
    (NULL,                                              'Subaru',     'Outback',   'AA0015BB', 'standard'),
    (NULL,                                              'Lexus',      'RX',        'AA0016BB', 'business'),
    (NULL,                                              'Audi',       'A4',        'AA0017BB', 'business'),
    (NULL,                                              'Mitsubishi', 'Lancer',    'AA0018BB', 'standard'),
    (NULL,                                              'Citroen',    'C4',        'AA0019BB', 'standard'),
    (NULL,                                              'Peugeot',    '308',       'AA0020BB', 'standard');