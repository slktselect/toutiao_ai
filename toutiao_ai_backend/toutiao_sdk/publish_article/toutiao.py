import requests

from settings import TOUTIAO_SETTING

url = "https://mp.toutiao.com/mp/agw/article/publish?source=mp&type=article&aid=1231&_signature=_02B4Z6wo00101eeZ-vwAAIDAOMIJsAaDyKXnnf5AAB6TQcnoSRUipVWaA7QIZmknyS3RNru3WN-fAQpeivsmfOlOXbNsPc-ONa.FQlRkJfvfDD04dHuwn9S0eROBqkkpfufYwasNgPRvLDqg61&msToken=_yZ3Nvsw27epa6xbR9w208lyPViUA3he10kXPQHAl4JqCYpJv6DaIuif1H2mR7E1Ph8S8f_FGMoVpmtSS_TSyoks_c8yGUDFwFwz7_kYEiT-U12_Dfqfogw8mvzcEf42I7xn9Ym7yGSshJ87sHb4L0k7YwAkoEcfefHzqjICismS&a_bogus=E705keUjxqAnad-rmKDry4VU9L9lNBSyeaiQRCqI7oFpGhMGY5PFiqWiaFou6fhtf8B7otV72fREExjaQsSUXcPkKsZvSoGfI0%2FAIzfo8qi3T0tQLHmmC8kzKwsG0YUF-QCGElv51sse2dQWVN9wAQ17L%2F3rRRjdMq-tVMTnT9KmUWWjkx%2Fna5LDFhA4"

payload='pgc_id=7455510149537530380&source=0&content=%3Cp%20data-track%3D%221%22%3Eaewf%3C%2Fp%3E%3Cp%20data-track%3D%222%22%3Esrhthjerstjuhrtyser5tujhr5t6yju56yejudrtjur76tkio8lu7ie56y7ju%3C%2Fp%3E%3Cp%20data-track%3D%221%22%3Eaewf%3C%2Fp%3E%3Cp%20data-track%3D%226%22%3Esrhthjerstjuhrtyser5tujhr5t6yju56yejudrtjur76tkio8lu7ie56y7ju%3C%2Fp%3E%3Cp%20data-track%3D%227%22%3E%3Cbr%3E%3C%2Fp%3E%3Cp%20data-track%3D%221%22%3Eaewf%3C%2Fp%3E%3Cp%20data-track%3D%228%22%3Esrhthjerstjuhrtyser5tujhr5t6yju56yejudrtjur76tkio8lu7ie56y7ju%3C%2Fp%3E%3Cp%20data-track%3D%229%22%3Eaewf%3C%2Fp%3E%3Cp%20data-track%3D%2210%22%3Esrhthjerstjuhrtyser5tujhr5t6yju56yejudrtjur76tkio8lu7ie56y7ju%3C%2Fp%3E&title=awef&search_creation_info=%7B%22searchTopOne%22%3A0%2C%22abstract%22%3A%22%22%2C%22clue_id%22%3A%22%22%7D&title_id=1735871231189_1819569590647820&ic_uri_list=&extra=%7B%22content_word_cnt%22%3A130%2C%22is_multi_title%22%3A0%2C%22sub_titles%22%3A%5B%5D%2C%22manual_selected_city%22%3A%22%7B%5C%22city%5C%22%3A%5C%22%E8%81%8A%E5%9F%8E%5C%22%2C%5C%22city_code%5C%22%3A%5C%22371500%5C%22%7D%22%2C%22gd_ext%22%3A%7B%22entrance%22%3A%22%22%2C%22from_page%22%3A%22publisher_mp%22%2C%22enter_from%22%3A%22PC%22%2C%22device_platform%22%3A%22mp%22%2C%22is_message%22%3A0%7D%2C%22tuwen_wtt_trans_flag%22%3A%220%22%2C%22info_source%22%3A%7B%22source_type%22%3A3%2C%22source_author_uid%22%3A%22%22%2C%22time_format%22%3A%22%22%2C%22position%22%3A%7B%7D%7D%7D&appid_list=&stock_ids=&concern_list=&mp_editor_stat=%7B%7D&is_refute_rumor=0&save=1&timer_status=0&timer_time=&educluecard=&draft_form_data=%7B%22coverType%22%3A2%7D&pgc_feed_covers=%5B%7B%22id%22%3A%22%22%2C%22url%22%3A%22https%3A%2F%2Fimage-tt-private.toutiao.com%2Ftos-cn-i-6w9my0ksvp%2F10e5a4419360460eb37e57269104abeb~tplv-tt-cover-v2.image%3F_iz%3D115383%26c%3D811c9dc5%26from%3Dimage_upload%26lk3s%3D72284de7%26policy%3DeyJ2bSI6MywidWlkIjoiODQ2NzQ2NTgzODYifQ%253D%253D%26x-orig-authkey%3D5a21e4afda5945d9a206a695e4c78a63%26x-orig-expires%3D2367023290%26x-orig-sign%3D31PK3f8Qmvi0IWJfJ%252FK5bp7Zavc%253D%22%2C%22uri%22%3A%22tos-cn-i-6w9my0ksvp%2F995f7fc5f72f426f9f5027fe0885a88c%22%2C%22ic_uri%22%3A%22%22%2C%22thumb_width%22%3A1920%2C%22thumb_height%22%3A1080%2C%22extra%22%3A%7B%22from_content_uri%22%3A%22%22%2C%22from_content%22%3A%220%22%7D%7D%5D&article_ad_type=3&is_fans_article=0&govern_forward=0&praise=0&disable_praise=0&tree_plan_article=0&star_order_id=&star_order_name=&activity_tag=0&trends_writing_tag=0&claim_exclusive=1'
headers = {
   'priority': 'u=1, i',
   'x-secsdk-csrf-token': '000100000001bd120890f29b546aedd5be03b3ca4d8ba2631af0a78649e8e458942c86a3534618170db00f61e0cb',
   'Cookie': TOUTIAO_SETTING["Cookie"],
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
   'Accept': '*/*',
   'Host': 'mp.toutiao.com',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)