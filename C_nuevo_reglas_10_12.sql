SET DEFINE OFF;
update tbpcrules set expression ='myObj.getItem().getCurrentOAType().getCode().compareTo("CH")==0 
&& myObj.getItem().getPODynProp("Product").compareTo("PortePagado")!=0
&& ((myObj.getItem().hasChildByCaption("SimCard")==true 
&& myObj.getItem().getChildByCaption("SimCard").isNewItem()==true)
&& myObj.getItem().getChildByCaption("SimCard").getAttribute("AcquisitionType").compareTo("Triangulado")==0)
&& myObj.getItem().getAttribute("PortingInd").compareTo("Y")==0'
where groupid = '167583177_0' and ref_type = 'IT' and pcversion_id >= '40015010';


update tbpcrules set expression ='(myObj.getItem().getOrderActionVal()!=null 
&& myObj.getItem().getOrderActionType()!=null 
&& myObj.getItem().getOrderActionType().getCode().compareTo("PR")==0 
&& myObj.getItem().getOrderActionVal().getParentRelationVal().getCode().compareTo("AM")!=0) 
&& ((myObj.getItem().getChildByCaption("Access")!=null
&& myObj.getItem().getChildByCaption("Access").getAttribute("Network_Technology")!=null
&& myObj.getItem().getChildByCaption("Access").getAttribute("Network_Technology").compareTo("COBRE")==0) 
|| (myObj.getItem().getProductInOrderByName("245373")!=null
&& myObj.getItem().getProductInOrderByName("245373").getChildByCaption("Broadband_Plan").getDoubleAttribute("Download_Speed")>20)) 
&& (myObj.getUser().getSecurityProfileIdVal()!= null 
&& (myObj.getUser().getSecurityProfileIdVal().compareTo("BOFFMAN")==0 
|| myObj.getUser().getSecurityProfileIdVal().compareTo("BOFFANA")==0))'
where groupid = '119661475_0' and ref_type = 'IT' and pcversion_id >= '40015010';


update tbpcrules set expression ='myObj.getItem().getAttribute("APN_Type").compareTo()!=null
&&  myObj.getItem().getAttribute("APN_Type").compareTo("Dedicated")==0 
&& (myObj.getItem().getAttribute("APN_Name").compareTo("M2M.movistar")==0 
|| myObj.getItem().getAttribute("APN_Name").compareTo("VPN.movistar")==0)'
where groupid = '99674445_0' and ref_type = 'IT' and pcversion_id >= '40015010';


update tbpcrules set expression ='myObj.getItem().getCurrentOAType().getCode().compareTo("CH")==0 
&& myObj.getItem().getPODynProp("Product").compareTo("PortePagado")==0 
&& ((myObj.getItem().hasChildByCaption("SimCard")==true 
&& myObj.getItem().getChildByCaption("SimCard").isNewItem()==true)
&& myObj.getItem().getChildByCaption("SimCard").getAttribute("AcquisitionType").compareTo("Triangulado")==0)
&& myObj.getItem().getAttribute("PortingInd").compareTo("Y")==0'
where groupid = '167582877_0' and ref_type = 'IT' and pcversion_id >= '40015010';


update tbpcrules set expression ='myObj.getItem().getOrderActionVal()!=null 
&& myObj.getItem().getCurrentOAType().getCode()!=null
&& (myObj.getItem().getCurrentOAType().getCode().compareTo("PR")==0
|| myObj.getItem().isReplaceOffer()==true
|| myObj.getItem().getCurrentOAType().getCode().compareTo("CW")==0)
&& myObj.getCustomer().getIsAnonymous()==false
&& (myObj.getCustomer().getCustomerBillingSubType().compareTo("ETP")==0
|| myObj.getCustomer().getCustomerBillingSubType().compareTo("EG")==0
|| myObj.getCustomer().getCustomerBillingSubType().compareTo("ER")==0
|| myObj.getCustomer().getCustomerBillingSubType().compareTo("EY")==0)
&& myObj.getItem().getPODynProp("LOB Type")!=null
&& myObj.getItem().getPODynProp("LOB Type").compareTo("WRLS")==0
&& myObj.getItem().getPODynProp("PSA Code").compareTo("CGN011")==0'
where groupid = '168756477_0' and ref_type = 'IT' and pcversion_id >= '40015010';


update tbpcrules set expression ='myObj.getItem().hideAvailablePricePlan("Plan","Descuento60_6mesesenPlanMovilPromo")'
where groupid = '168066477_0' and ref_type = 'OS' and pcversion_id >= '40015010';


update tbpcrules set expression='myObj.getItem().setAttribute("Notification_Email",myObj.getCustomer().getcontact().getEmailVal())'
where groupid = '118756575_0' and ref_type = 'OS' and pcversion_id >= '40015010';

update tbpcrules set expression='(myObj.getItem().isNewItem()==true 
&& (myObj.getItem().getAttribute("Notification_Email")== null 
|| myObj.getItem().getAttribute("Notification_Email").trim().compareTo("")==0)) 
|| (myObj.getItem().isNewItem()!=true 
&& (myObj.getItem().getCurrentOAType().getCode().compareTo("CW")==0 
|| (myObj.getItem().getAttribute("Notification_Email")!= null  
&& myObj.getItem().getAttribute("Notification_Email").compareTo(myObj.getCustomer().getcontact().getEmailVal())!=0)))'
where groupid = '118756575_0' and ref_type = 'IT' and pcversion_id >= '40015010';

COMMIT;