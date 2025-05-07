select p.id, p.numero, p.questao, p.tipo, i.nome from tb_pergunta p left join tb_item i on p.id = i.pergunta_id where enquete_id = 1

select * from tb_item;