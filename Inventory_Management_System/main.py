{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a954ca65",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-42155c638ef6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    144\u001b[0m   {\n\u001b[0;32m    145\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 146\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    147\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"333dbca3\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    148\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "{\n",
    " \"cells\": [\n",
    "  {\n",
    "   \"cell_type\": \"code\",\n",
    "   \"execution_count\": 2,\n",
    "   \"id\": \"40e61e6c\",\n",
    "   \"metadata\": {},\n",
    "   \"outputs\": [\n",
    "    {\n",
    "     \"name\": \"stdout\",\n",
    "     \"output_type\": \"stream\",\n",
    "     \"text\": [\n",
    "      \"===========================================================================\\n\",\n",
    "      \"                            INVENTARY MANAGEMENT\\n\",\n",
    "      \"===========================================================================\\n\",\n",
    "      \"\\n\",\n",
    "      \"\\t\\tEnter 1 for See the Products\\n\",\n",
    "      \"\\t\\tEnter 2 for Update the Products\\n\",\n",
    "      \"\\t\\tEnter 3 for Puchase the Products\\n\",\n",
    "      \"\\t\\tEnter 4 for See Sales Products\\n\",\n",
    "      \"\\t\\tEnter 5 for Exit\\n\",\n",
    "      \"\\n\",\n",
    "      \"\\t\\tEnter Your Choice : 1\\n\",\n",
    "      \"                                     PRODUCTS LIST\\n\",\n",
    "      \"\\n\",\n",
    "      \"\\t\\tProduct Id.     Product Name         Price           Quantity  \\n\"\n",
    "     ]\n",
    "    },\n",
    "    {\n",
    "     \"ename\": \"TypeError\",\n",
    "     \"evalue\": \"list indices must be integers or slices, not str\",\n",
    "     \"output_type\": \"error\",\n",
    "     \"traceback\": [\n",
    "      \"\\u001b[1;31m---------------------------------------------------------------------------\\u001b[0m\",\n",
    "      \"\\u001b[1;31mTypeError\\u001b[0m                                 Traceback (most recent call last)\",\n",
    "      \"\\u001b[1;32m<ipython-input-2-e2c1b5d770cf>\\u001b[0m in \\u001b[0;36m<module>\\u001b[1;34m\\u001b[0m\\n\\u001b[0;32m     29\\u001b[0m         \\u001b[0mprint\\u001b[0m\\u001b[1;33m(\\u001b[0m\\u001b[1;34m\\\"\\\\n\\\\t\\\\t%-15s %-20s %-15s %-10s\\\"\\u001b[0m\\u001b[1;33m%\\u001b[0m \\u001b[1;33m(\\u001b[0m\\u001b[1;34m\\\"Product Id.\\\"\\u001b[0m \\u001b[1;33m,\\u001b[0m\\u001b[1;34m\\\"Product Name\\\"\\u001b[0m\\u001b[1;33m,\\u001b[0m\\u001b[1;34m\\\"Price\\\"\\u001b[0m\\u001b[1;33m,\\u001b[0m \\u001b[1;34m\\\"Quantity\\\"\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[0m\\n\\u001b[0;32m     30\\u001b[0m         \\u001b[1;32mfor\\u001b[0m \\u001b[0mi\\u001b[0m \\u001b[1;32min\\u001b[0m \\u001b[0mrecords\\u001b[0m\\u001b[1;33m.\\u001b[0m\\u001b[0mkeys\\u001b[0m\\u001b[1;33m(\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m:\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[0m\\n\\u001b[1;32m---> 31\\u001b[1;33m             \\u001b[0mprint\\u001b[0m\\u001b[1;33m(\\u001b[0m\\u001b[1;34m\\\"\\\\t\\\\t%-15s %-20s %-15f %-10d\\\"\\u001b[0m\\u001b[1;33m%\\u001b[0m \\u001b[1;33m(\\u001b[0m\\u001b[0mi\\u001b[0m\\u001b[1;33m,\\u001b[0m\\u001b[0mrecords\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[0mi\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[1;34m'name'\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m,\\u001b[0m\\u001b[0mrecords\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[0mi\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[1;34m'pr'\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m,\\u001b[0m\\u001b[0mrecords\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[0mi\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m[\\u001b[0m\\u001b[1;34m'qn'\\u001b[0m\\u001b[1;33m]\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[0m\\n\\u001b[0m\\u001b[0;32m     32\\u001b[0m         \\u001b[0mrecord_file\\u001b[0m\\u001b[1;33m.\\u001b[0m\\u001b[0mclose\\u001b[0m\\u001b[1;33m(\\u001b[0m\\u001b[1;33m)\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[1;33m\\u001b[0m\\u001b[0m\\n\\u001b[0;32m     33\\u001b[0m \\u001b[1;33m\\u001b[0m\\u001b[0m\\n\",\n",
    "      \"\\u001b[1;31mTypeError\\u001b[0m: list indices must be integers or slices, not str\"\n",
    "     ]\n",
    "    }\n",
    "   ],\n",
    "   \"source\": [\n",
    "    \"#importig json package\\n\",\n",
    "    \"import json\\n\",\n",
    "    \"#Function to Create Line\\n\",\n",
    "    \"def line():\\n\",\n",
    "    \"    print(\\\"===========================================================================\\\")\\n\",\n",
    "    \"\\n\",\n",
    "    \"#Function to create heading\\n\",\n",
    "    \"def heading(str):\\n\",\n",
    "    \"    print(\\\"                            \\\"+str)\\n\",\n",
    "    \"\\n\",\n",
    "    \"\\n\",\n",
    "    \"line()\\n\",\n",
    "    \"heading(\\\"INVENTARY MANAGEMENT\\\")\\n\",\n",
    "    \"line()\\n\",\n",
    "    \"while(1):\\n\",\n",
    "    \"    print(\\\"\\\\n\\\\t\\\\tEnter 1 for See the Products\\\")\\n\",\n",
    "    \"    print(\\\"\\\\t\\\\tEnter 2 for Update the Products\\\")\\n\",\n",
    "    \"    print(\\\"\\\\t\\\\tEnter 3 for Puchase the Products\\\")\\n\",\n",
    "    \"    print(\\\"\\\\t\\\\tEnter 4 for See Sales Products\\\")\\n\",\n",
    "    \"    print(\\\"\\\\t\\\\tEnter 5 for Exit\\\")\\n\",\n",
    "    \"    choice=input(\\\"\\\\n\\\\t\\\\tEnter Your Choice : \\\")\\n\",\n",
    "    \"\\n\",\n",
    "    \"    #For See the Product\\n\",\n",
    "    \"    if(choice=='1'):\\n\",\n",
    "    \"        record_file = open(\\\"record.json\\\",'r')\\n\",\n",
    "    \"        record_data = record_file.read()\\n\",\n",
    "    \"        records= json.loads(record_data)\\n\",\n",
    "    \"        heading(\\\"         PRODUCTS LIST\\\")\\n\",\n",
    "    \"        print(\\\"\\\\n\\\\t\\\\t%-15s %-20s %-15s %-10s\\\"% (\\\"Product Id.\\\" ,\\\"Product Name\\\",\\\"Price\\\", \\\"Quantity\\\"))\\n\",\n",
    "    \"        for i in records.keys():\\n\",\n",
    "    \"            print(\\\"\\\\t\\\\t%-15s %-20s %-15f %-10d\\\"% (i,records[i]['name'],records[i]['pr'],records[i]['qn']))\\n\",\n",
    "    \"        record_file.close()\\n\",\n",
    "    \"\\n\",\n",
    "    \"    elif(choice=='2'):\\n\",\n",
    "    \"        record_file = open(\\\"record.json\\\",'r')\\n\",\n",
    "    \"        record_data = record_file.read()\\n\",\n",
    "    \"        record_file.close()\\n\",\n",
    "    \"        records= json.loads(record_data)\\n\",\n",
    "    \"        prod_id =input(\\\"\\\\t\\\\tEnter product id : \\\")\\n\",\n",
    "    \"        product_name = input(\\\"\\\\t\\\\tEnter name : \\\")\\n\",\n",
    "    \"        product_pr = float(input(\\\"\\\\t\\\\tEnter price : \\\"))\\n\",\n",
    "    \"        product_qn = int(input(\\\"\\\\t\\\\tEnter quantity : \\\"))\\n\",\n",
    "    \"        records[prod_id] = {'name': product_name, 'pr': product_pr, 'qn': product_qn}\\n\",\n",
    "    \"        all_data = json.dumps(records)\\n\",\n",
    "    \"        record_file = open(\\\"record.json\\\",'w')\\n\",\n",
    "    \"        record_file.write(all_data)\\n\",\n",
    "    \"        record_file.close()\\n\",\n",
    "    \"\\n\",\n",
    "    \"    elif(choice=='3'):\\n\",\n",
    "    \"        record_file = open(\\\"record.json\\\",'r')\\n\",\n",
    "    \"        record_data = record_file.read()\\n\",\n",
    "    \"        record_file.close()\\n\",\n",
    "    \"        records= json.loads(record_data)\\n\",\n",
    "    \"        ui_prod  = input(\\\"\\\\t\\\\tEnter the product_Id: \\\")\\n\",\n",
    "    \"        ui_quant = int(input(\\\"\\\\t\\\\tEnter the quantity: \\\"))\\n\",\n",
    "    \"        #For validating the number of product is more or not\\n\",\n",
    "    \"        if(records[ui_prod]['qn']>=ui_quant):\\n\",\n",
    "    \"            print(\\\"\\\\n\\\\t\\\\t\\\\t|Product: \\\", records[ui_prod]['name'])\\n\",\n",
    "    \"            print(\\\"\\\\t\\\\t\\\\t|Price: \\\", records[ui_prod]['pr'])\\n\",\n",
    "    \"            print(\\\"\\\\t\\\\t\\\\t|Billing Amount: \\\", records[ui_prod]['pr'] * ui_quant)\\n\",\n",
    "    \"            print(\\\"\\\\t\\\\t\\\\t|Please Visit Again (*_*) \\\")\\n\",\n",
    "    \"            records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant\\n\",\n",
    "    \"\\n\",\n",
    "    \"            record_file = open(\\\"record.json\\\",'w')\\n\",\n",
    "    \"            all_data = json.dumps(records)\\n\",\n",
    "    \"            record_file.write(all_data)\\n\",\n",
    "    \"            record_file.close()\\n\",\n",
    "    \"\\n\",\n",
    "    \"            #Opening sales.json data in read mode\\n\",\n",
    "    \"            sales_file = open(\\\"sales.json\\\",'r')\\n\",\n",
    "    \"            sales_data= sales_file.read()\\n\",\n",
    "    \"            sales_file.close()\\n\",\n",
    "    \"            record= json.loads(sales_data)\\n\",\n",
    "    \"            record[len(record)+1] = {'name':records[ui_prod]['name'], 'pr':records[ui_prod]['pr'], 'qn':ui_quant}\\n\",\n",
    "    \"            #Opening sales.json file in writing mode to update the sales product\\n\",\n",
    "    \"            sales_file = open(\\\"sales.json\\\",'w')\\n\",\n",
    "    \"            all_data_sales = json.dumps(record)\\n\",\n",
    "    \"            sales_file.write(all_data_sales)\\n\",\n",
    "    \"            sales_file.close()\\n\",\n",
    "    \"        else:\\n\",\n",
    "    \"            print(\\\"\\\\n\\\\t\\\\t Sorry!! We have only \\\"+str(records[ui_prod]['qn'])+\\\" Product!!\\\")\\n\",\n",
    "    \"\\n\",\n",
    "    \"    #To see the sale.json data\\n\",\n",
    "    \"    elif(choice=='4'):\\n\",\n",
    "    \"        sales_file = open(\\\"sales.json\\\",'r')\\n\",\n",
    "    \"        sales_data = sales_file.read()\\n\",\n",
    "    \"        records= json.loads(sales_data)\\n\",\n",
    "    \"        heading(\\\"SELL PRODUCTS LIST\\\")\\n\",\n",
    "    \"        print(\\\"\\\\n\\\\t\\\\t%-15s %-20s %-15s %-10s\\\"% (\\\"Product Id.\\\" ,\\\"Product Name\\\",\\\"Price\\\", \\\"Quantity\\\"))\\n\",\n",
    "    \"        for i in records.keys():\\n\",\n",
    "    \"            print(\\\"\\\\t\\\\t%-15s %-20s %-15f %-10d\\\"% (i,records[i]['name'],records[i]['pr'],records[i]['qn']))\\n\",\n",
    "    \"        sales_file.close()\\n\",\n",
    "    \"\\n\",\n",
    "    \"    #To Exit\\n\",\n",
    "    \"    elif(choice=='5'):\\n\",\n",
    "    \"        break\\n\",\n",
    "    \"\\n\",\n",
    "    \"    #Invalid Choice\\n\",\n",
    "    \"    else:\\n\",\n",
    "    \"        print(\\\"Invalid Choice!!\\\")\"\n",
    "   ]\n",
    "  },\n",
    "  {\n",
    "   \"cell_type\": \"code\",\n",
    "   \"execution_count\": null,\n",
    "   \"id\": \"333dbca3\",\n",
    "   \"metadata\": {},\n",
    "   \"outputs\": [],\n",
    "   \"source\": []\n",
    "  }\n",
    " ],\n",
    " \"metadata\": {\n",
    "  \"kernelspec\": {\n",
    "   \"display_name\": \"Python 3\",\n",
    "   \"language\": \"python\",\n",
    "   \"name\": \"python3\"\n",
    "  },\n",
    "  \"language_info\": {\n",
    "   \"codemirror_mode\": {\n",
    "    \"name\": \"ipython\",\n",
    "    \"version\": 3\n",
    "   },\n",
    "   \"file_extension\": \".py\",\n",
    "   \"mimetype\": \"text/x-python\",\n",
    "   \"name\": \"python\",\n",
    "   \"nbconvert_exporter\": \"python\",\n",
    "   \"pygments_lexer\": \"ipython3\",\n",
    "   \"version\": \"3.8.8\"\n",
    "  }\n",
    " },\n",
    " \"nbformat\": 4,\n",
    " \"nbformat_minor\": 5\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51be7a12",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
