#!/usr/bin/python
# -*- coding: UTF-8 -*-


wordsdict = {}
langs = "en zh zh_cn zh_tw fr ru ar es de pt ja ko hi".split(" ")
words = ['author', 'url', 'hashtags', 'others', 'single', 'translated', 'workspace', 'pc', 'monitor', 'tool', 'scanner', 'tablet', 'mouse', 'printer', 'desktop', 'music', 'desk', 'chair', 'comment']


# 整合多个存放翻译的dict
def getWordsDict():
	dict1 = {
		'en': {'author': 'author', 'url': 'URL', 'hashtags': 'hashtags', 'others': 'others'},
		'zh': {'author': '作者', 'url': '网址', 'hashtags': '标签', 'others': '其他'},
		'zh_cn': {'author': '作者', 'url': '网址', 'hashtags': '标签', 'others': '其他'},
		'zh_tw': {'author': '作者', 'url': '網址', 'hashtags': '標籤', 'others': '其他'},
		'ja': {'author': '著者', 'url': 'URL', 'hashtags': 'ハッシュタグ', 'others': 'その他'},
		'ko': {'author': '작가', 'url': 'URL', 'hashtags': '해시태그', 'others': '기타'},
		'fr': {'author': 'auteur', 'url': 'URL', 'hashtags': 'hashtags', 'others': 'les autres'},
		'de': {'author': 'Autor', 'url': 'URL', 'hashtags': 'Hashtags', 'others': 'Andere'},
		'ru': {'author': 'автор', 'url': 'URL', 'hashtags': 'хэштеги', 'others': 'другие'},
		'es': {'author': 'autor', 'url': 'URL', 'hashtags': 'etiquetas', 'others': 'otros'},
		'pt': {'author': 'autor', 'url': 'URL', 'hashtags': 'hashtags', 'others': 'outros'},
		'hi': {'author': 'लेखक', 'url': 'यूआरएल', 'hashtags': 'हैशटैग', 'others': 'अन्य'},
		}
	
	dict2 = {
		"en": {"single": "Single", "translated": "Translated"},
		"zh": {"single": "单篇", "translated": "翻译"},
		"zh_cn": {"single": "单篇", "translated": "翻译"},
		"zh_tw": {"single": "單篇", "translated": "翻譯"},
		"fr": {'single': 'histoire unique', 'translated': 'Traduction'},
		"ru": {'single': 'отдельная история', 'translated': 'перевод'},
		"ar": {'single': 'قصة واحدة', 'translated': 'ترجمة'},
		"es": {'single': 'sola historia', 'translated': 'traducción'},
		"de": {'single': 'einzelne Geschichte', 'translated': 'Übersetzung'},
		"pt": {'single': 'história única', 'translated': 'tradução'},
		"ja": {'single': '一話', 'translated': '翻訳'},
		"ko": {'single': '단 하나의 이야기', 'translated': '번역'},
		"hi": {'single': 'एकल कहानी', 'translated': 'अनुवाद'},
		}
	
	dict3 = {
		 'en': {'workspace': 'Workspace', 'pc': 'Computer', 'monitor': 'monitor', 'tool': 'Software', 'scanner': 'Scanner', 'tablet': 'Graphic tablet', 'mouse': 'Mouse', 'printer': 'Printer', 'desktop': 'Things on your desk', 'music': 'Background music', 'desk': 'Table', 'chair': 'chair', 'comment': 'Others'},
		"zh": {'workspace': '创作环境', 'pc': '电脑', 'monitor': '显示器', 'tool': '软件', 'scanner': '扫描仪', 'tablet': '数位板','mouse': '鼠标', 'printer': '打印机', 'desktop': '桌面物品', 'music': '音乐', 'desk': '桌子', 'chair': '椅子','comment': '其他'},
		 "zh_cn": {'workspace': '创作环境', 'pc': '电脑', 'monitor': '显示器', 'tool': '软件', 'scanner': '扫描仪', 'tablet': '数位板','mouse': '鼠标', 'printer': '打印机', 'desktop': '桌面物品', 'music': '音乐', 'desk': '桌子', 'chair': '椅子', 'comment': '其他'},
		 "zh_tw": {'workspace': '創作環境', 'pc': '電腦', 'monitor': '監視器', 'tool': '軟體', 'scanner': '掃描儀', 'tablet': '繪圖板','mouse': '滑鼠', 'printer': '打印機', 'desktop': '桌面物品', 'music': '音樂', 'desk': '桌子', 'chair': '椅子', 'comment': '其他'},
	    'fr': {'workspace': 'Espace de travail', 'pc': "L'ordinateur", 'monitor': 'Moniteur', 'tool': 'Logiciel', 'scanner': 'Scanner', 'tablet': 'Tablette graphique', 'mouse': 'Souris', 'printer': 'Imprimante', 'desktop': 'Choses sur votre bureau', 'music': 'Musique de fond', 'desk': 'desk', 'chair': 'Chaise', 'comment': 'Les autres'},
	    'ru': {'workspace': 'Рабочее пространство', 'pc': 'Компьютер', 'monitor': 'Монитор', 'tool': 'Программного обеспечения', 'scanner': 'Сканер', 'tablet': 'Графический планшет', 'mouse': 'мышь', 'printer': 'принтер', 'desktop': 'Вещи на вашем столе', 'music': 'Фоновая музыка', 'desk': 'Стол', 'chair': 'Стул', 'comment': 'Другие'},
	    'ar': {'workspace': 'مساحة العمل', 'pc': 'الحاسوب', 'monitor': 'مراقب', 'tool': 'برمجة', 'scanner': 'الماسح الضوئي', 'tablet': 'لوحة الرسم', 'mouse': 'الفأر', 'printer': 'طابعة', 'desktop': 'أشياء على مكتبك', 'music': 'خلفيه موسيقية', 'desk': 'الطاولة', 'chair': 'كرسي', 'comment': 'آحرون'},
	    'es': {'workspace': 'espacio de trabajo', 'pc': 'Computadora', 'monitor': 'monitor', 'tool': 'tool', 'scanner': 'Escáner', 'tablet': 'Tableta gráfica', 'mouse': 'Ratón', 'printer': 'Impresora', 'desktop': 'cosas en tu escritorio', 'music': 'Música de fondo', 'desk': 'Mesa', 'chair': 'Silla', 'comment': 'Otros'},
	    'de': {'workspace': 'Arbeitsplatz', 'pc': 'pc', 'monitor': 'monitor', 'tool': 'tool', 'scanner': 'Scanner', 'tablet': 'Grafiktablet', 'mouse': 'Maus', 'printer': 'Drucker', 'desktop': 'Dinge auf Ihrem Schreibtisch', 'music': 'Hintergrundmusik', 'desk': 'Tisch', 'chair': 'Stuhl', 'comment': 'Andere'},
	    'pt': {'workspace': 'Área de trabalho', 'pc': 'Computador', 'monitor': 'monitor', 'tool': 'Programas', 'scanner': 'Scanner', 'tablet': 'Mesa digitalizadora', 'mouse': 'Rato', 'printer': 'Impressora', 'desktop': 'Coisas em sua mesa', 'music': 'Música de fundo', 'desk': 'Mesa', 'chair': 'Cadeira', 'comment': 'Outros'},
	    'ja': {'workspace': 'ワークスペース', 'pc': 'コンピューター', 'monitor': 'モニター', 'tool': 'ソフトウェア', 'scanner': 'スキャナ', 'tablet': 'グラフィックタブレット', 'mouse': 'ねずみ', 'printer': 'プリンター', 'desktop': 'あなたの机の上にあるもの', 'music': 'バックグラウンドミュージック', 'desk': 'テーブル', 'chair': '椅子', 'comment': 'その他'},
	    'ko': {'workspace': '작업 공간', 'pc': '컴퓨터', 'monitor': '감시 장치', 'tool': '소프트웨어', 'scanner': '스캐너', 'tablet': '그래픽 태블릿', 'mouse': '생쥐', 'printer': '인쇄기', 'desktop': '책상 위의 것들', 'music': '배경 음악', 'desk': '테이블', 'chair': '의자', 'comment': '기타'},
		'hi': {'workspace': 'कार्यस्थान', 'pc': 'संगणक', 'monitor': 'निगरानी करना', 'tool': 'सॉफ़्टवेयर', 'scanner': 'चित्रान्वीक्षक', 'tablet': 'ग्राफिक टैबलेट', 'mouse': 'चूहा', 'printer': 'मुद्रक', 'desktop': 'आपके डेस्क पर मौजूद चीज़ें', 'music': 'पार्श्व संगीत', 'desk': 'मेज', 'chair': 'कुर्सी', 'comment': 'अन्य'}
		}
	
	words = []
	dicts = [dict1, dict2, dict3,]
	for lang1 in langs:
		d0 = {}
		for d1 in dicts:
			# print(d1)
			for lang2, d2 in d1.items():
				if lang1 == lang2:
					# print(lang1, d2)
					d0.update(d2)
					for key in d2:
						if key not in words:
							words.append(key)
		wordsdict[lang1] = d0

	
if True:
	getWordsDict()


if __name__ == '__main__':
	print(len(words), words, sep="\n")
	# print(wordsdict)
	pass