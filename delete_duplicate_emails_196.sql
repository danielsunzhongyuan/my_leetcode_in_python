delete from Person
where Person.Id not in (
    select p1.Id
    from (
        select min(p2.Id) as Id, p2.Email
        from Person p2
        group by p2.Email
    ) p1
)
