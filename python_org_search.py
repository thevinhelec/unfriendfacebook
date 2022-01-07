# -*- coding: utf-8 -*-
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument("--user-data-dir=C:\\Users\\vinh.nong\\AppData\\Local\\Google\\Chrome\\User Data")
op.add_argument("--profile-directory=Profile 1")
op.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=ser, chrome_options=op)

# option
INSPECT_FRIEND_LIST = False
INSPECT_POST = True
UNFRIEND = False
# get friend list

print ("get friend list start")

friend_list = []
if INSPECT_FRIEND_LIST == False:
    print ("read fiend list from friend.txt")
    with open('friend.txt', 'r') as filein:
        friend_list = json.load(filein)
else:
    print ("get friend list from facebook.com")
    driver.get('https://www.facebook.com/me/friends_all')

    time.sleep(10) # Let the user actually see something!

    loading_friends_panel_class = "lzcic4wl j83agx80 btwxx1t3 lhclo0ds i1fnvgqd"
    loading_friends_panel_selector = f"div[class='{loading_friends_panel_class}'][data-visualcompletion='loading-state']"

    loading_element = driver.find_elements(By.CSS_SELECTOR,
        loading_friends_panel_selector
    )

    while len(loading_element) > 0:
        print ("loading friend list ...")
        driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
        time.sleep(10)
        loading_element = driver.find_elements(By.CSS_SELECTOR,
            loading_friends_panel_selector)
    print ("loading friend list done")
    time.sleep(10)
    friends_panel_selector = "div[data-pagelet='ProfileAppSection_0']"

    friends_pannel = driver.find_element(By.CSS_SELECTOR,
        friends_panel_selector)

    friend_link_class = (
        "oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l q9uorilb lzcic4wl pioscnbf wkznzc2l l9j0dhe7 etr7akla"
    )

    friend_link_selector = f"a[class='{friend_link_class}']"

    friend_links = friends_pannel.find_elements(By.CSS_SELECTOR,
        friend_link_selector)

    for friend_link in friend_links:
        link = friend_link.get_attribute("href")
        friend_list.append(
            dict(
                link=link,
                hadLike=False,
                hadComment=False,
                numberOfLike=0,
                numberOfComment=0
            )
        )

for friend in friend_list:
    print (friend["link"])
with open('friend.txt', 'w') as fileout:
     json.dump(friend_list, fileout)
print(f"Number of friends: {len(friend_list)}")
print ("get friend list done")
# done get friend 
# get post list

print ("get post list")
post_panels = []
if INSPECT_POST == True:
    driver.get('https://www.facebook.com/me')

    time.sleep(10) # Let the user actually see something!

    loading_posts_panel_class = "lzcic4wl sjgh65i0 k4urcfbm"
    loading_posts_panel_selector = f"div[class='{loading_posts_panel_class}'][data-visualcompletion='loading-state']"

    loading_element = driver.find_elements(By.CSS_SELECTOR,
        loading_posts_panel_selector
    )

    while len(loading_element) > 0:
        print ("loading profile time line ...")
        driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
        time.sleep(4)
        loading_element = driver.find_elements(By.CSS_SELECTOR,
            loading_posts_panel_selector)
    print ("loading profile time line done")

    profile_Timeline_selector = "div[data-pagelet='ProfileTimeline']"

    profile_Timeline_pannel = driver.find_element(By.CSS_SELECTOR,
        profile_Timeline_selector)

    post_panel_class = (
    "du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"
    )

    post_panel_class_selector = f"div[class='{post_panel_class}']"

    post_panels = profile_Timeline_pannel.find_elements(By.CSS_SELECTOR,
        post_panel_class_selector)

    print(f"Number of posts: {len(post_panels)}")

    post_index = 0

    print ("get post list done")
        #get list posts done

    for post in post_panels:
        print (f"inspect post {post_index} th")
        driver.execute_script("arguments[0].scrollIntoView(true);", post)
        time.sleep(1)
        try:
            print (f" inspect like of post")
            post_like_link_class = (
                "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l lzcic4wl gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs a8c37x1j"
            )

            post_like_link_selector = f"div[class='{post_like_link_class}']"
            post_like_link = post.find_element(By.CSS_SELECTOR,
                post_like_link_selector)
            print (" This post have like")
            driver.execute_script("arguments[0].scrollIntoView(true);", post_like_link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", post_like_link)
            print ("  click post_like_link")
            time.sleep(3)

            like_popup_panel_element_class = "l9j0dhe7 du4w35lb cjfnh4rs j83agx80 cbu4d94t lzcic4wl ni8dbmo4 stjgntxs oqq733wu cwj9ozl2 io0zqebd m5lcvass fbipl8qg nwvqtn77 nwpbqux9 iy3k6uwz e9a99x49 g8p4j16d bv25afu3 gc7gaz0o k4urcfbm"
            like_popup_panel_element_selector = f"div[class='{like_popup_panel_element_class}'][role='dialog']"
            like_popup_panel = driver.find_element(By.CSS_SELECTOR, like_popup_panel_element_selector) 
            try:
                scroll_element_class = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"
                scroll_element_selector = f"a[class='{scroll_element_class}'][role='link']"
                scroll_element = like_popup_panel.find_element(By.CSS_SELECTOR,scroll_element_selector)
            except:
                print("  Error: can not find any element")

            loading_like_panel_class = "lzcic4wl afxn4irw r8dsh44q ee40wjg4 skuavjfj ku44ohm1 g6srhlxm lszeityy sb3519qa n99xedck jnigpg78 l82x9zwi uo3d90p7 pw54ja7n ue3kfks5"
            loading_like_panel_selector = f"div[class='{loading_like_panel_class}'][data-visualcompletion='loading-state']"

            loading_element = like_popup_panel.find_elements(By.CSS_SELECTOR,
                loading_like_panel_selector)
            print (f"  Number of loading_like_panel_selector: {len(loading_element)}")

            while len(loading_element) > 0:
                print ("  loading like list ...")
                scroll_element = like_popup_panel.find_element(By.CSS_SELECTOR, scroll_element_selector)
                scroll_element.send_keys(Keys.END)
                time.sleep(4)
                loading_element = driver.find_elements(By.CSS_SELECTOR,
                    loading_like_panel_selector)
            print ("  loading like list done")
            
            people_elements = like_popup_panel.find_elements(By.CSS_SELECTOR, scroll_element_selector) 
            page_link = ""
            for p in people_elements:
        
                link = p.get_attribute("href")
                if "profile.php" in link:
                    page_link = link[0:55:1]
                else:
                    indexofquestionmark = link.find("?")
                    page_link = link[0:indexofquestionmark:1]

                    for friend in friend_list:
                        if friend["link"] == page_link:
                            friend["hadLike"] = True
                            friend["numberOfLike"] += 1
                            break
                print (f"   Name of people liked: {page_link}")
            print (f"  number of like: {len(people_elements)}")
            close_button_element_class = "hu5pjgll m6k467ps"
            close_button_element_selector = f"i[class='{close_button_element_class}'][data-visualcompletion='css-img']"
            close_button = like_popup_panel.find_element(By.CSS_SELECTOR,close_button_element_selector) 
            driver.execute_script("arguments[0].click();", close_button)
            print ("  click close_button")
            time.sleep(3)

        except:
            print ("  This post not have like_link")
        print (f" inspect like of post done")
        print (f" inspect comment of post")

        comment_panel_class = "cwj9ozl2 tvmbv18p"
        comment_panel_selector = f"div[class='{comment_panel_class}']"
        comment_panel_element = post.find_element(By.CSS_SELECTOR,
            comment_panel_selector)
    
        see_more_comment_class = (
            "oajrlxb2 g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh lzcic4wl bp9cbjyn m9osqain buofh1pr g5gj957u p8fzw8mz gpro0wi8"
        )
        see_more_comment_selector = f"div[class='{see_more_comment_class}']"

        see_more_comment_link_elements = comment_panel_element.find_elements(By.CSS_SELECTOR,
            see_more_comment_selector)
        print (f"  number of see_more_comment_link_elements: {see_more_comment_link_elements}")
        if len(see_more_comment_link_elements) > 0:
            print ("  have see more/hide comment link")
            had_see_more_comment_link = True
            while had_see_more_comment_link:
                print ("  load more comment ...")
                see_more_comment_link_elements = comment_panel_element.find_elements(By.CSS_SELECTOR,
                    see_more_comment_selector)
                had_see_more_comment_link = False
                for see_more_comment_link in see_more_comment_link_elements:
                    innerText = see_more_comment_link.get_attribute('innerText')
                    print (f"  inner text of element: {innerText}")
                    if 'Ẩn' not in innerText:
                        had_see_more_comment_link = True
                        print ("  click on see more comment link")
                        driver.execute_script("arguments[0].scrollIntoView(true);", see_more_comment_link)
                        time.sleep(10)
                        driver.execute_script("arguments[0].click();", see_more_comment_link)
                        time.sleep(10)
                        break
                    else:
                        print ("  this is hide comment, not click")
        print ("  load more comment done")

        comment_class = (
        "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8"
        )

        comment_selector = f"a[class='{comment_class}']"

        comment_links = comment_panel_element.find_elements(By.CSS_SELECTOR,
            comment_selector)
    
        print (f"  number of comment: {len(comment_links)}")
        page_link = ""
        for comment in comment_links:
            link = comment.get_attribute("href")
            if "profile.php" in link:
                page_link = link[0:55:1]
            else:
                indexofquestionmark = link.find("?")
                page_link = link[0:indexofquestionmark:1]

                for friend in friend_list:
                    if friend["link"] == page_link:
                        friend["hadComment"] = True
                        friend["numberOfComment"] += 1
                        break
            print (f"   Name of people commented: {page_link}")

        print (f" inspect comment of post done")
        print (f"inspect post {post_index} th done")
        post_index +=1
    with open('friend.txt', 'w') as fileout:
        json.dump(friend_list, fileout)


print ("result")
numberOfAccountNeverLikeOrComment = len(friend_list)
totalNumberOfLike = 0
totalNumberOfComment = 0
for friend in friend_list:
    print (f"friend link: {friend['link']}, hadlike: {friend['hadLike']}, numberOfLike: {friend['numberOfLike']}, hadComment: {friend['hadComment']}, numberOfComment: {friend['numberOfComment']}")
    totalNumberOfLike += friend['numberOfLike']
    totalNumberOfComment += friend['numberOfComment']
    if friend['hadLike'] == True or friend['hadComment'] == True:
        numberOfAccountNeverLikeOrComment -= 1

print ("Sumary:")
print(f"Number of friends: {len(friend_list)}")
print(f"Number of posts: {len(post_panels)}")
print (f"total Number Of Like: {totalNumberOfLike}")
print (f"total Number Of Comment: {totalNumberOfComment}")
print (f"number of friend need to unfriend: {numberOfAccountNeverLikeOrComment}")

print (type(friend_list[0]))

rank = 20
like_most_list = sorted (friend_list, key = lambda i: i['numberOfLike'],reverse=True)
print (f"the {rank} people who like the most")
for x in range(rank):
    print (f" rank {x}th : {like_most_list[x]['link']}, like: {like_most_list[x]['numberOfLike']} times")

comment_most_list = sorted (friend_list, key = lambda i: i['numberOfComment'],reverse=True)
print (f"the {rank} people who comment the most")
for x in range(rank):
    print (f" rank {x}th : {comment_most_list[x]['link']}, comment: {comment_most_list[x]['numberOfComment']} times")

# start unfriend process

if UNFRIEND == True:
    print (f"Do you want to see list of friend who never like or comment ({numberOfAccountNeverLikeOrComment} people) ")
    print ("type Y to see")
    x= input()
    if x == 'Y':
        for friend in friend_list:
            if friend['hadComment'] == False and friend['hadLike'] == False:
                print (f"friend link: {friend['link']}")

    print (f"Do you want to unfriend all friend who never like or comment ({numberOfAccountNeverLikeOrComment} people) ")
    print ("type Y to unfriend all")
    x= input()
    if x == 'Y':
        for friend in friend_list:
            if friend['hadComment'] == False and friend['hadLike'] == False:
                driver.get(friend['link'])
                time.sleep(2)
                friend_button_class = (
                    "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l lzcic4wl rq0escxv pq6dq46d cbu4d94t taijpn5t l9j0dhe7 k4urcfbm"
                )
                friend_button_selector = f"div[class='{friend_button_class}'][aria-label='Bạn bè']"
                friend_button = driver.find_element(By.CSS_SELECTOR,
                    friend_button_selector)
                driver.execute_script("arguments[0].click();", friend_button)
                time.sleep(1)

                unfriend_button_class = (
                    "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz p7hjln8o esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l lzcic4wl dwo3fsh8 rq0escxv nhd2j8a9 j83agx80 btwxx1t3 pfnyh3mw opuu4ng7 kj2yoqh6 kvgmc6g5 oygrvhab l9j0dhe7 i1ao9s8h du4w35lb bp9cbjyn cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr"
                )

                unfriend_button_selector = f"div[class='{unfriend_button_class}']"
                unfriend_buttons = driver.find_elements(By.CSS_SELECTOR,
                    unfriend_button_selector)

                for unfriend_button in unfriend_buttons:
                    innerText = unfriend_button.get_attribute('innerText')
                    if "Hủy kết bạn" in innerText:
                        driver.execute_script("arguments[0].click();", unfriend_button)
                        time.sleep(2)
                        confirm_button_class = (
                            "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l lzcic4wl rq0escxv pq6dq46d cbu4d94t taijpn5t l9j0dhe7 k4urcfbm"
                        )
                        confirm_button_selector = f"div[class='{confirm_button_class}'][aria-label='Xác nhận']"
                        confirm_button = driver.find_element(By.CSS_SELECTOR,
                            confirm_button_selector)
                        driver.execute_script("arguments[0].click();", confirm_button)
                        time.sleep(2)


    else:
        for friend in friend_list:
            if friend['hadComment'] == False and friend['hadLike'] == False:
                driver.get(friend['link'])
                time.sleep(2)
                print (f"Do you want unfriend: {friend['link']}")
                print ("type Y to unfriend")
                x= input()
                if x == 'Y':
                    print (f"Unfriend: {friend['link']}")
                

time.sleep(5) # Let the user actually see something!

print ("End of program")
x= input()
driver.quit()
