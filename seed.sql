INSERT INTO accounts (nom, type) VALUES
    ('Compte courant', 'courant'),
    ('Livret A', 'epargne');

INSERT INTO categories (nom) VALUES
    ('Restos'), ('Achat en ligne'), ('Courses'), ('Loisirs'), ('Abonnement');

INSERT INTO transactions (date, libelle, montant, account_id, category_id) VALUES
    ('2026-10-01', 'Bourse',        250000, 1, NULL),
    ('2026-10-03', 'Restaurant',     -1850,  1, 1),
    ('2026-10-05', 'TBM',         -8640,  1, 2),
    ('2026-11-02', 'Supermarché',    -6420,  1, 3),
    ('2026-11-08', 'Virement inconnu', -3000, 1, NULL),
    ('2026-10-09', 'Cinéma',          -1200,  1, 4),
    ('2026-10-12', 'Supermarché',     -5430,  1, 3),
    ('2026-10-15', 'Netflix',         -1399,  1, 5),
    ('2026-10-20', 'Amazon',          -2999,  1, 2),
    ('2026-10-28', 'Pizzeria',        -2400,  1, 1),
    ('2026-11-01', 'Bourse',          250000, 1, NULL),
    ('2026-11-04', 'Restaurant',      -3200,  1, 1),
    ('2026-11-06', 'Spotify',         -1199,  1, 5),
    ('2026-11-10', 'Supermarché',     -4875,  1, 3),
    ('2026-11-12', 'Kebab',           -950,   1, 1),
    ('2026-11-14', 'Remboursement',   1500,   1, NULL),
    ('2026-11-15', 'Netflix',         -1399,  1, 5),
    ('2026-11-17', 'Bowling',         -2200,  1, 4),
    ('2026-11-19', 'Fnac en ligne',   -4590,  1, 2),
    ('2026-11-20', 'Épargne mensuelle', 10000, 2, NULL);


SELECT c.nom AS categorie, SUM(t.montant) AS total
FROM transactions t
LEFT JOIN categories c ON t.category_id = c.id
WHERE t.date >= date_trunc('month', CURRENT_DATE)
  AND t.date <  date_trunc('month', CURRENT_DATE) + INTERVAL '1 month'
  AND t.montant < 0
GROUP BY c.nom
ORDER BY total ASC;
