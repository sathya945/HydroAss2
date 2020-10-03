import math

def q1(attr):
    ph =0.11
    temp=0.10
    turb=0.08
    tdv=0.07
    nitrates=0.10
    fecalcol =0.16
    # assuming we have q normalized values
    print(attr["ph"],attr["temp"],attr["turb"],attr["tdv"],attr["nitrates"],attr["fecalcol"])
    wqi = ph*attr["ph"]+temp*attr["temp"]+turb*attr["turb"]+tdv*attr["tdv"]+nitrates*attr["nitrates"]+fecalcol*attr["fecalcol"]
    wqi = wqi/(ph+temp+turb+tdv+nitrates+fecalcol)

    return wqi


def q2(attr):
    # assuming we take mean of existing attributes
    cnt=0
    param_vals = []
    if "Turbidity" in attr:
        cnt+=1
        val=attr["Turbidity"]
        if val<=5:
            param_vals.append(1)
        elif val>5 and val<=10:
            param_vals.append(val/5)
        elif val>10 and val<=500:
            param_vals.append((43.9+val)/34.5)
    
    if "pH" in attr:
        cnt+=1
        val=attr["pH"]
        if val==7:
            param_vals.append(1)
        elif val>7:
            param_vals.append(math.exp((val-7)/1.082))
        else:
            param_vals.append(math.exp((7-val)/1.082))
    
    if "Coliform" in attr:
        cnt+=1
        val=attr["Coliform"]
        if val>=10 and val<150:
            param_vals.append((val+130)/140)
        elif val>=150 and val<=1200:
            param_vals.append(val/75)
    
    if "DO" in attr:
        cnt+=1
        val=attr["DO"]
        if val<50:
            param_vals.append(math.exp((98.33-val)/36.067))
        elif val>=50 and val<=100:
            param_vals.append((val-107.58)/14.667)
        else:
            param_vals.append((val-79.543)/19.054)
    
    if "BOD" in attr:
        cnt+=1;
        val=attr["BOD"]
        if val<2:
            param_vals.append(1)
        elif val>=2 and val<=30:
            param_vals.append(val/1.5)
    
    if "TDS" in attr:
        cnt+=1
        val=attr["TDS"]
        if val<=500:
            param_vals.append(1)
        elif val>500 and val<=1500:
            param_vals.append(math.exp((val-500)/721.5))
        elif val>1500 and val<=3000:
            param_vals.append((val-1000)/125)
        elif val>3000 and val<=6000:
            param_vals.append(val/375)

    if "Hardness" in attr:
        cnt+=1;
        val=attr["Hardness"]
        if val<=75:
            param_vals.append(1)
        elif val>75 and val<=500:
            param_vals.append(math.exp((val+42.5)/205.58))
        elif val>500:
            param_vals.append((val+500)/125)
        
    if "Cl" in attr:
        cnt+=1
        val=attr["Cl"]
        if val<=150:
            param_vals.append(1)
        elif val>150 and val<=250:
            param_vals.append(math.exp(((val/50)-3)/1.4427))
        elif val>250:
            param_vals.append(math.exp(((val/50)+10.167)/10.82))

    if "No3" in attr:
        cnt+=1
        val=attr["No3"]
        if val<=20:
            param_vals.append(1)
        elif val>20 and val<=50:
            param_vals.append(math.exp((val-145.16)/76.28))
        elif val>50 and val<=200:
            param_vals.append(val/65)
    
    if "So4" in attr:
        cnt+=1
        val = attr["So4"]
        if val<=150:
            param_vals.append(1)
        elif val>150 and val<=2000:
            param_vals.append(((val/50) + 0.375)/2.5121)
        
    if "Coliform" in attr:
        cnt+=1
        val = attr["Coliform"]
        if val<=50:
            param_vals.append(1)
        elif val>50 and val<=5000:
            param_vals.append((val/50)**(0.3010))
        elif val>5000 and val<=15000:
            param_vals.append(((val/50)-50)/16.071)
        else :
            param_vals.append((val/15000) + 16)
    
    if "As" in attr:
        cnt+=1
        val = attr["As"]
        if val<=0.005:
            param_vals.append(1)
        elif val>0.005 and val<0.01:
            param_vals.append(val/0.005)
        elif val>=0.01 and val<0.1:
            param_vals.append((val + 0.015)/0.0146)
        elif val>=0.1 and val<=1.3:
            param_vals.append((val + 1.1)/0.15)
    
    if "F" in attr:
        cnt+=1
        val = attr["F"]
        if val>=0 and val<1.2:
            param_vals.append(1)
        elif val>=1.2 and val<=10:
            param_vals.append(((val/1.2) - 0.3819)/0.5083)
    
    wqi=0
    for i in param_vals:
        wqi+=i
    
    wqi/=cnt

    return wqi

        
def q1_main(e1,e2,e3,e4,e5,e6):
    params = {}
    params["ph"] = e1
    params["temp"] = e2
    params["turb"] = e3
    params["tdv"] = e4
    params["nitrates"] = e5
    params["fecalcol"] = e6

    return q1(params)

        
def q2_main(ets):
    params = {}
    # use the same atts array as in gui.py
    atts = ["Turbidity", "pH","Color","DO", "BOD","TDS", "Hardness","Cl","No3","So4","Coliform","As","F"]

    for i in range(len(ets)):
        params[atts[i]] = ets[i]

    return q2(params)