import random

data = [
	'भँवर',
	'रेम्बो',
	'जल्दी करना',
	'शानदार',
	'पिक्सी-बॉब',
	'बेकार',
	'जियोडक',
	'दासता',
	'प्रवाहित',
	'जानकार',
	'ब्रोंकोस्कोपी',
	'आईना',
	'उजाड़ देना',
	'कटौती',
	'कटाक्ष',
	'व्यंग्य',
	'इंटरकॉम',
	'आधार',
	'फोटोरिअलिस्ट',
	'पिघल गया',
	'रूसियों',
	'सर्दी का मौसम',
	'सेरानो',
	'जागना',
	'ग्लाइकोजेनोलिटिक',
	'फरीसियों',
	'मैथुन करने वाला',
	'प्रॉपिंग',
	'जल-त्वचा',
	'पानी-नया',
	'सहवास करना',
	'तार से',
	'ओथडोक्सी',
	'खिलना',
	'युद्ध-चील',
	'रीछ',
	'बेरुखी',
	'कैद',
	'अविभाज्यता',
	'जार्डन',
	'एकता',
	'गैर-अपराधिक',
	'समझ में आ',
	'कैफीनिज्म',
	'सुपाच्य',
	'टाइटेनिया',
	'मज़हब',
	'प्लॉबॉय',
	'शौक रखने वाला',
	'आडंबर',
	'नॉनस्पेक्ट्रिक',
	'मेमोरीअप',
	'तिरछा',
	'छाना हुआ',
	'ध्यान',
	'सर्वव्यापी',
	'अभिमानी',
	'नाइट्रोक्स',
	'बहता है',
	'आगे बढ़ना',
	'पेप्टिडर्जिक',
	'अपमानजनक',
	'शराब बनाना',
	'झालरदार',
	'बहकाना',
	'पूवे',
	'श्रद्धा',
	'उदात्त',
	'साबूदाना',
	'फिर से लागू करना',
	'अव्यक्त',
	'अग्रगामी',
	'गौ-पालन',
	'परिवर्तन',
	'डनम',
	'पूर्ववर्ती',
	'कुढ़ना-मार्टीन',
	'फॉक्स फायर'
]

def hindi_random():
	x = random.randint(0, len(data))
	return data[x]