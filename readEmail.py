{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'emailAddress': 'herambh.yad@gmail.com', 'messagesTotal': 724, 'threadsTotal': 635, 'historyId': '181833'}\n",
      "Message snippets:\n",
      "\n",
      "\n",
      "\n",
      " {'id': '1700add6f97e0b2b', 'threadId': '1700add6f97e0b2b', 'labelIds': ['CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Dear Herambh, Thank you for applying for the position of R-061234 Data Sciences &amp; AI Graduate Programme - US. We are currently reviewing the applications and will be back in touch with you soon. We', 'historyId': '180977', 'internalDate': '1580730248000', 'payload': {'mimeType': 'multipart/mixed', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@myworkday.com header.s=0szq2t2p3 header.b=FRIqM+w9;       spf=pass (google.com: domain of astrazeneca@myworkday.com designates 37.0.1.161 as permitted sender) smtp.mailfrom=astrazeneca@myworkday.com;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=myworkday.com'}, {'name': 'Subject', 'value': 'Thank you for your application'}]}, 'sizeEstimate': 16630}\n",
      "\n",
      "\n",
      "\n",
      " Email Address of Sender:-  astrazeneca@myworkday.com\n",
      "\n",
      "\n",
      "Subject:-  'Thank you for your application'\n",
      "\n",
      "\n",
      "\n",
      " {'id': '16eff76a39726ba6', 'threadId': '16eff76a39726ba6', 'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Dear Herambh, Thank you for applying for the position of R-061234 Data Sciences &amp; AI Graduate Programme - US. We just wanted to let you know that we are still reviewing your application and we will', 'historyId': '156237', 'internalDate': '1576243994000', 'payload': {'mimeType': 'multipart/mixed', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@myworkday.com header.s=0s2q2t2p3 header.b=Og+o7T2b;       spf=pass (google.com: domain of astrazeneca@myworkday.com designates 37.0.1.161 as permitted sender) smtp.mailfrom=astrazeneca@myworkday.com;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=myworkday.com'}, {'name': 'Subject', 'value': 'Thank you for your application'}]}, 'sizeEstimate': 16937}\n",
      "\n",
      "\n",
      "\n",
      " Email Address of Sender:-  astrazeneca@myworkday.com\n",
      "\n",
      "\n",
      "Subject:-  'Thank you for your application'\n",
      "\n",
      "\n",
      "\n",
      " {'id': '16e02a3527934e76', 'threadId': '16e02a3527934e76', 'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Dear Herambh, Thank you for your interest in career opportunities with Deloitte Consulting LLP and the Data Scientist - Helena, MT -- E20ROSCPDMJE95905-SA position. Unfortunately, after careful', 'historyId': '180985', 'internalDate': '1572002283000', 'payload': {'mimeType': 'multipart/alternative', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=2; mx.google.com;       dkim=pass header.i=@deloitte.com header.s=us1 header.b=itQ4XVMw;       arc=pass (i=1 spf=pass spfdomain=deloitte.com dkim=pass dkdomain=deloitte.com dmarc=pass fromdomain=deloitte.com);       spf=pass (google.com: domain of usrecruiting2@deloitte.com designates 68.232.140.227 as permitted sender) smtp.mailfrom=usrecruiting2@deloitte.com;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=deloitte.com'}, {'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.microsoft.com 1; spf=pass smtp.mailfrom=deloitte.com; dmarc=pass action=none header.from=deloitte.com; dkim=pass header.d=deloitte.com; arc=none'}, {'name': 'Subject', 'value': 'Data Scientist - Helena, MT at Deloitte Consulting LLP'}]}, 'sizeEstimate': 59533}\n",
      "\n",
      "\n",
      "\n",
      " Email Address of Sender:-  usrecruiting2@deloitte.com\n",
      "\n",
      "\n",
      "Subject:-  'Data Scientist - Helena, MT at Deloitte Consulting LLP'\n",
      "\n",
      "\n",
      "\n",
      " {'id': '16dd503681b0db4f', 'threadId': '16dd503681b0db4f', 'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Hi Herambh, Thank you for your interest in the Data Scientist position at viagogo and taking the time to apply. Unfortunately, due to the large number of highly qualified applicants, we are unable to', 'historyId': '68895', 'internalDate': '1571236832000', 'payload': {'mimeType': 'multipart/alternative', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@gh-mail.viagogo.com header.s=krs header.b=LR9GqLHI;       dkim=pass header.i=@mailgun.org header.s=mg header.b=3Ytllf3h;       spf=pass (google.com: domain of postmaster@gh-mail.viagogo.com designates 209.61.151.40 as permitted sender) smtp.mailfrom=postmaster@gh-mail.viagogo.com;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=viagogo.com'}, {'name': 'Subject', 'value': 'Viagogo Application Outcome'}]}, 'sizeEstimate': 6536}\n",
      "\n",
      "\n",
      "\n",
      " Email Address of Sender:-  postmaster@gh-mai\n",
      "\n",
      "\n",
      "Subject:-  'Viagogo Application Outcome'\n",
      "\n",
      "\n",
      "\n",
      " {'id': '16d955133c7fdec2', 'threadId': '16d955133c7fdec2', 'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Hi Herambh Thank you for your time, unfortunately at this stage we will not be progressing with your application for the Entry Level Data Analytics, Northeast # role. Please do ensure that you keep', 'historyId': '181262', 'internalDate': '1570168005000', 'payload': {'mimeType': 'multipart/alternative', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@recruiting.avanade.com header.s=avat1 header.b=wlsWJvel;       spf=pass (google.com: domain of bounces-ajhmylikgb44ayi806hd96bfzwnhdjwb@avanade.avature.net designates 209.137.158.189 as permitted sender) smtp.mailfrom=bounces-AjhmYLIkGb44ayi806hD96bFzwnhDjwb@avanade.avature.net;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=recruiting.avanade.com'}, {'name': 'Subject', 'value': 'Update on your Application - Avanade'}]}, 'sizeEstimate': 179184}\n",
      "\n",
      "\n",
      "\n",
      " Email Address of Sender:-  ajhmylikgb44ayi806hd96bfzwnhdjwb@avanade.ava\n",
      "\n",
      "\n",
      "Subject:-  'Update on your Application - Avanade'\n",
      "\n",
      "\n",
      "\n",
      " {'id': '16d93a537f441689', 'threadId': '16d93a537f441689', 'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 'snippet': 'Hello Herambh, Thank you for expressing interest in iCIMS and the Data Scientist position for which you have applied. While we were impressed with your qualifications, unfortunately we have decided to', 'historyId': '50534', 'internalDate': '1570140137000', 'payload': {'mimeType': 'multipart/alternative', 'headers': [{'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@talent.icims.com header.s=icims-platform1 header.b=2WjCb9hf;       spf=pass (google.com: domain of msprvs1=18179xxf6zgy_=bounces-265138-1@bounces-corp.icims.com designates 147.253.212.8 as permitted sender) smtp.mailfrom=\"msprvs1=18179xXf6ZGY_=bounces-265138-1@bounces-corp.icims.com\";       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=talent.icims.com'}, {'name': 'Subject', 'value': 'Data Scientist Application at iCIMS'}]}, 'sizeEstimate': 21469}\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'group'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-99-5361bfcbebc7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    106\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    107\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 108\u001b[1;33m \u001b[0mrejects_ids\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma_i_ids\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreject_subject\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma_i_subject\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mout1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mout2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcategorise\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-99-5361bfcbebc7>\u001b[0m in \u001b[0;36mcategorise\u001b[1;34m()\u001b[0m\n\u001b[0;32m     51\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'\\n\\n\\n'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     52\u001b[0m             \u001b[0mout1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmsg\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 53\u001b[1;33m             \u001b[0memail_add\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mout1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     54\u001b[0m             \u001b[0mrejects_ids\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'id'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     55\u001b[0m             \u001b[0mmsg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-99-5361bfcbebc7>\u001b[0m in \u001b[0;36memail_add\u001b[1;34m(out)\u001b[0m\n\u001b[0;32m     15\u001b[0m     \u001b[1;31m# print(s)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 17\u001b[1;33m     \u001b[0memails\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msearch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpattern\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgroup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     18\u001b[0m     \u001b[0mmatchList\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0memails\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'group'"
     ]
    }
   ],
   "source": [
    "from googleapiclient.discovery import build\n",
    "from httplib2 import Http\n",
    "from oauth2client import file, client, tools\n",
    "import re\n",
    "\n",
    "SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'\n",
    "\n",
    "def email_add(out):\n",
    "    \n",
    "\n",
    "    pattern = r'[a-zA-Z0-9]{4,}@[a-zA-Z0-9]{,}.[a-z]{1,3}'\n",
    "\n",
    "    s = out\n",
    "\n",
    "    # print(s)\n",
    "\n",
    "    emails = re.search(pattern, s).group()\n",
    "    matchList = str(emails).split(' ')\n",
    "\n",
    "    for email in matchList:\n",
    "        print('\\n\\n\\n Email Address of Sender:- ',email)\n",
    "\n",
    "\n",
    "def categorise():\n",
    "   \n",
    "    store = file.Storage('token.json')\n",
    "    creds = store.get()\n",
    "    if not creds or creds.invalid:\n",
    "        flow = client.flow_from_clientsecrets('client_secret_514215414527-hhhruimjvtvtjpru4c8uai2o5uc4ujsa.apps.googleusercontent.com.json', SCOPES)\n",
    "        creds = tools.run_flow(flow, store)\n",
    "    service = build('gmail', 'v1', http=creds.authorize(Http()))\n",
    "    \n",
    "    # Call the Gmail API to fetch INBOX for REJECTS\n",
    "    possible_rejects = service.users().messages().list(userId='me',labelIds = ['INBOX','CATEGORY_UPDATES'], q = 'unfortunately' or 'regret').execute()\n",
    "    messages = possible_rejects.get('messages', [])\n",
    "    rejects_ids = []\n",
    "    a_i_ids = []\n",
    "    reject_subject = []\n",
    "    a_i_subject = []\n",
    "    userInfo = service.users().getProfile(userId='me').execute()\n",
    "    print(userInfo)\n",
    "    \n",
    "\n",
    "    if not messages:\n",
    "        print (\"No messages found.\")\n",
    "    else:\n",
    "        print (\"Message snippets:\")\n",
    "        for message in messages:\n",
    "            msg = service.users().messages().get(userId='me', id=message['id'], format='metadata', metadataHeaders=[\"Subject\",\"ARC-Authentication-Results\"]).execute()\n",
    "            #print ('\\nEmail Snippet:- ',msg['snippet'])\n",
    "            print('\\n\\n\\n',msg)\n",
    "            out1 = msg\n",
    "            email_add(str(out1))\n",
    "            rejects_ids.append(msg['id'])\n",
    "            msg = str(msg)\n",
    "            #print(type(msg))\n",
    "            msg = msg.rsplit(\"'Subject', 'value': \")\n",
    "            msg = msg[1]\n",
    "            msg = msg.rsplit(\"}]},\")\n",
    "            final1 = msg[0]\n",
    "            print('\\n\\nSubject:- ',final1)\n",
    "            reject_subject.append(final1)\n",
    "            \n",
    "            #print('\\nEmail Subject:- ',msg['payload']['headers'][var]['value'])\n",
    "            #print('\\n\\n\\n\\n\\n\\n',msg['labelIds'][0])\n",
    "            \n",
    "            \n",
    "            \n",
    "     \n",
    "    \n",
    "    # Call the Gmail API to fetch INBOX for ACCEPTANCE/INTERVIEW INVITATIONS\n",
    "    print('\\n\\n\\n\\n\\n\\n\\n\\n\\n')\n",
    "    possible_accepts = service.users().messages().list(userId='me',labelIds = ['INBOX','CATEGORY_UPDATES'], q = 'assessment' or 'congratulations' or 'interview' or 'coding' or 'phone' or 'video' or 'call').execute()\n",
    "    messages2 = possible_accepts.get('messages', [])\n",
    "\n",
    "    #userInfo = service.users().getProfile(userId='me').execute()\n",
    "    #print(userInfo)\n",
    "    \n",
    "\n",
    "    if not messages2:\n",
    "        print (\"No messages found.\")\n",
    "    else:\n",
    "        print (\"Message snippets:\")\n",
    "        for message in messages2:\n",
    "            msg2 = service.users().messages().get(userId='me', id=message['id'], format='metadata', metadataHeaders=[\"Subject\",\"ARC-Authentication-Results\"]).execute()\n",
    "            #print ('\\nEmail Snippet:- ',msg2['snippet'])\n",
    "            #print('\\n\\n\\n',msg2)\n",
    "            out2 = msg2\n",
    "            email_add(str(out2))\n",
    "            a_i_ids.append(msg2['id'])\n",
    "            msg2 = str(msg2)\n",
    "            #print(type(msg2))\n",
    "            msg2 = msg2.rsplit(\"'Subject', 'value': \")\n",
    "            msg2 = msg2[1]\n",
    "            msg2 = msg2.rsplit(\"}]},\")\n",
    "            final2 = msg2[0]\n",
    "            print('\\n\\nSubject:- ',final2)\n",
    "            a_i_subject.append(final2)\n",
    "            #print('\\nEmail Subject:- ',msg2['payload']['headers'][var]['value'])\n",
    "            #print('\\n\\n\\n\\n\\n\\n',msg2['labelIds'][0])\n",
    "            \n",
    "    return rejects_ids, a_i_ids, reject_subject, a_i_subject, out1, out2\n",
    "\n",
    "#if __name__ == '__main__':\n",
    "#    main()\n",
    "\n",
    "\n",
    "rejects_ids, a_i_ids, reject_subject, a_i_subject, out1, out2 = categorise()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1700add6f97e0b2b', '16eff76a39726ba6', '16e02a3527934e76', '16dd503681b0db4f', '16d955133c7fdec2', '16d93a537f441689', '16d9281814207ed3', '16d5f7ee97dbfe73'] \n",
      "\n",
      "\n",
      " [\"'Thank you for your application'\", \"'Thank you for your application'\", \"'Data Scientist - Helena, MT at Deloitte Consulting LLP'\", \"'Viagogo Application Outcome'\", \"'Update on your Application - Avanade'\", \"'Data Scientist Application at iCIMS'\", \"'Application follow-up: Carvana'\", \"'Your application to Data Scientist - Analytics, Trust at Airbnb'\"] \n",
      "\n",
      "\n",
      " ['1700add6f97e0b2b', '16f8fe411d857f6d', '16eff76a39726ba6', '16e855c5fd43edbe', '16e600fd3f4dd56d', '16e4c9100521a97c', '16e1ac8097985182', '16e1413bba77b441', '16debdead6e22efb', '16debdc91baf26e0', '16db14020852d439', '16da697a9a4d8ebe', '16d8c60434bfb772', '16d8b80ea914daf1', '16d6d35ec4ae5f21'] \n",
      "\n",
      "\n",
      " [\"'Thank you for your application'\", \"'Thank you for your application - Hint & Tips on your Astrazeneca Assessment Day - Facebook Live event'\", \"'Thank you for your application'\", \"'Associate, Data Science-1905883 at santanderus (Santander Bank, N.A.)'\", \"'Information has changed for your assessment for Tresata'\", \"'Tresata assessment invitation - please complete'\", \"'P&G Careers - Application Completed'\", \"'American Credit Acceptance invites you to complete an assessment'\", \"'Re: Re: Final Reminder: Complete Rio Tinto'\", \"'Re: Re: Interview with Rio Tinto'\", \"'Final Reminder: Complete Rio Tinto'\", \"'Interview with Rio Tinto'\", \"'Rio Tinto - Application Assessment / Évaluation des candidatures - req32060 Graduate Data Science Engineer.'\", \"'Thank you for Starting a Job Application at CVS Health'\", \"'Thank you for Starting a Job Application at CVS Health'\"]\n"
     ]
    }
   ],
   "source": [
    "print(rejects_ids, '\\n\\n\\n', reject_subject, '\\n\\n\\n', a_i_ids, '\\n\\n\\n', a_i_subject)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Extract email address\n",
    "#DONOT RUN ANY CODE BELOW"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      " reply@airbnb.com\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'group'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-97-14cd4c793b05>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[0memail_add\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mout1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 19\u001b[1;33m \u001b[0memail_add\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mout2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-97-14cd4c793b05>\u001b[0m in \u001b[0;36memail_add\u001b[1;34m(out)\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;31m# print(s)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m     \u001b[0memails\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msearch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpattern\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgroup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m     \u001b[0mmatchList\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0memails\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'group'"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def email_add(out):\n",
    "    \n",
    "\n",
    "    pattern = r'[a-zA-Z0-9]{4,}@[a-zA-Z0-9]{,}.[a-z]{1,3}'\n",
    "\n",
    "    s = out\n",
    "\n",
    "    # print(s)\n",
    "\n",
    "    emails = re.search(pattern, s).group()\n",
    "    matchList = str(emails).split(' ')\n",
    "\n",
    "    for email in matchList:\n",
    "        print('\\n\\n\\n Email Address of Sender:- ',email)\n",
    "        \n",
    "email_add(str(out1))\n",
    "email_add(str(out2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from googleapiclient.discovery import build\n",
    "from httplib2 import Http\n",
    "from oauth2client import file, client, tools\n",
    "\n",
    "SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def main():\n",
    "   \n",
    "    store = file.Storage('token.json')\n",
    "    creds = store.get()\n",
    "    if not creds or creds.invalid:\n",
    "        flow = client.flow_from_clientsecrets('client_secret_514215414527-hhhruimjvtvtjpru4c8uai2o5uc4ujsa.apps.googleusercontent.com.json', SCOPES)\n",
    "        creds = tools.run_flow(flow, store)\n",
    "    service = build('gmail', 'v1', http=creds.authorize(Http()))\n",
    "    \n",
    "    # Call the Gmail API to fetch INBOX for REJECTS\n",
    "    possible_rejects = service.users().messages().list(userId='me',labelIds = ['INBOX','CATEGORY_UPDATES'], q = 'unfortunately' or 'regret').execute()\n",
    "    messages = possible_rejects.get('messages', [])\n",
    "    #rejects_ids = []\n",
    "    #a_i_ids = []\n",
    "    userInfo = service.users().getProfile(userId='me').execute()\n",
    "    print(userInfo)\n",
    "    \n",
    "\n",
    "    if not messages:\n",
    "        print (\"No messages found.\")\n",
    "    else:\n",
    "        print (\"Message snippets:\")\n",
    "        for message in messages:\n",
    "            msg = service.users().messages().get(userId='me', id=message['id']).execute()\n",
    "            print ('\\nEmail Snippet:- ',msg['snippet'])\n",
    "            print('\\n\\n\\n',msg)\n",
    "            #rejects_ids.append(msg['id'])\n",
    "            var = 'Subject'\n",
    "            print('\\nEmail Subject:- ',msg['payload']['headers'][var]['value'])\n",
    "            #print('\\n\\n\\n\\n\\n\\n',msg['labelIds'][0])\n",
    "            \n",
    "            \n",
    "            \n",
    "     \n",
    "    \n",
    "    # Call the Gmail API to fetch INBOX for ACCEPTANCE/INTERVIEW INVITATIONS\n",
    "    print('\\n\\n\\n\\n\\n\\n\\n\\n\\n')\n",
    "    possible_accepts = service.users().messages().list(userId='me',labelIds = ['INBOX','CATEGORY_UPDATES'], q = 'assessment' or 'congratulations' or 'interview' or 'coding' or 'phone' or 'video' or 'call').execute()\n",
    "    messages2 = possible_accepts.get('messages', [])\n",
    "\n",
    "    userInfo = service.users().getProfile(userId='me').execute()\n",
    "    print(userInfo)\n",
    "    \n",
    "\n",
    "    if not messages2:\n",
    "        print (\"No messages found.\")\n",
    "    else:\n",
    "        print (\"Message snippets:\")\n",
    "        for message in messages2:\n",
    "            msg2 = service.users().messages().get(userId='me', id=message['id']).execute()\n",
    "            print ('\\nEmail Snippet:- ',msg2['snippet'])\n",
    "            #print('\\n\\n\\n',msg2)\n",
    "            #a_i_ids.append(msg2['id'])\n",
    "            var = 'Subject'\n",
    "            print('\\nEmail Subject:- ',msg2['payload']['headers'][var]['value'])\n",
    "            #print('\\n\\n\\n\\n\\n\\n',msg2['labelIds'][0])\n",
    "            \n",
    "    #return rejects_ids, a_i_ids\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}