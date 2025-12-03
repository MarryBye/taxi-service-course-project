INSERT INTO transactions
    (user_id, balance_type, transaction_type, amount, order_id)
VALUES
    ((SELECT id FROM users WHERE login = 'vlukianov'), 'payment', 'credit', 100, NULL),
    ((SELECT id FROM users WHERE login = 'vlukianov'), 'payment', 'debit', 80,  NULL),
    ((SELECT id FROM users WHERE login = 'vlukianov'), 'payment', 'credit', 100, NULL),
    ((SELECT id FROM users WHERE login = 'vlukianov'), 'payment', 'credit', 100, NULL),
    ((SELECT id FROM users WHERE login = 'vlukianov'), 'payment', 'debit', 120, NULL),

    ((SELECT id FROM users WHERE login = 'ssmirnov'),  'payment', 'credit',  50,  NULL),
    ((SELECT id FROM users WHERE login = 'ssmirnov'),  'earning', 'credit', 300,  NULL),
    ((SELECT id FROM users WHERE login = 'ssmirnov'),  'earning', 'debit',  200, NULL),
    ((SELECT id FROM users WHERE login = 'ssmirnov'),  'payment', 'penalty', 20,  NULL),

    ((SELECT id FROM users WHERE login = 'oivanchenko'),'payment', 'credit', 200, NULL),
    ((SELECT id FROM users WHERE login = 'oivanchenko'),'payment', 'debit',  15,  NULL),
    ((SELECT id FROM users WHERE login = 'oivanchenko'),'payment', 'refund',  5,   NULL),

    ((SELECT id FROM users WHERE login = 'dhulman'),    'payment', 'credit', 30,  NULL),
    ((SELECT id FROM users WHERE login = 'dhulman'),    'payment', 'debit',  25,  NULL),

    ((SELECT id FROM users WHERE login = 'rbenevalov'), 'payment', 'credit', 100, NULL),
    ((SELECT id FROM users WHERE login = 'rbenevalov'), 'payment', 'debit',  40,  NULL),
    ((SELECT id FROM users WHERE login = 'rbenevalov'), 'payment', 'refund', 10,  NULL),

    ((SELECT id FROM users WHERE login = 'vdemchenko'), 'payment', 'credit', 150, NULL),
    ((SELECT id FROM users WHERE login = 'vdemchenko'), 'payment', 'debit',  60,  NULL),
    ((SELECT id FROM users WHERE login = 'vdemchenko'), 'earning', 'debit', 50,  NULL),

    ((SELECT id FROM users WHERE login = 'mabdul'),     'payment', 'credit', 20,  NULL),
    ((SELECT id FROM users WHERE login = 'mabdul'),     'payment', 'debit',  8,   NULL),

    ((SELECT id FROM users WHERE login = 'mverbitskii'),'earning', 'credit', 250, NULL),
    ((SELECT id FROM users WHERE login = 'mverbitskii'),'earning', 'debit',  100, NULL),

    ((SELECT id FROM users WHERE login = 'aklatchini'),'payment', 'credit', 500, NULL),
    ((SELECT id FROM users WHERE login = 'aklatchini'),'payment', 'debit',  60,  NULL),

    ((SELECT id FROM users WHERE login = 'kbombini'),  'payment', 'credit', 400, NULL),
    ((SELECT id FROM users WHERE login = 'kbombini'),  'earning', 'debit',  300, NULL),

    ((SELECT id FROM users WHERE login = 'nagent'),    'earning', 'credit', 180, NULL),
    ((SELECT id FROM users WHERE login = 'nagent'),    'payment', 'penalty', 30, NULL);