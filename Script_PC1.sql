set define off;
UPDATE pc1_charge_code SET  revenue_type = 'OC' where revenue_type is null;
commit;