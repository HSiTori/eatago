# **Eatago**
## Author
**Annie**  
e-mail:kmes9940723@gmail.com

## License
[MIT LICENSE](https://github.com/sitori8354/eatago/blob/main/LICENSE)
## Problem to Solve
Eatago is a website aims to becomes a personal life manager for everyone, and it focus on improving the economy behind the food delivery service growth due to Covid-19. 
### 1. Save Money Spent on Delivered Food
&#160; &#160; &#160; &#160;In order to avoid contacting with people, people tend to order in foods instead of buying foods by themselves; hence, a large amount of money were spent. Hoping to help people save money while ordering food deliveries, Eatago compares the food prices of two main food delivering platforms 'UberEATS' and 'Food panda'. After choosing food we feel like ordering, Eatago will tell us which platform we should choose.
### 2. Eat Healthier even with Delivered Food
&#160; &#160; &#160; &#160;Human beings have higher probabilities to stay indoors and do less exercises due to covid-19, which may do harm to our health.
####     (1) Record what We have Consumed 
&#160; &#160; &#160; &#160;Eatago helps record what we have eaten, users can view them in a specified page. The list helps them know what the eat lesser and know which kind of food they should eat more. It also let they know how much junk food they have devoured, preventing them from having too much junk food. 
####     (2) Notification While Ordering
&#160; &#160; &#160; &#160;It is known to all that drinks is not healthy to us, especially those with sugar. Whenever we order are at the page of ordering, Eatago tells us how many drinks we have already drunk. The accumulation also works with late night suppers and garbage foods as well. Once any kind of them were ordered over twice in the recent ten orderings, Eatago will warn the user in hope of maintaining our health.
## Techniques We Use
### 1. Web Crawling:
&#160; &#160; &#160; &#160;To get a list of store names, merchandises, prices and other related information. The information were then used to build databases. 
1. Crawling of Food panda:  
&#160; &#160; &#160; &#160;Beautifulsoup package allowed us to analysis the html file of Food panda. We could get name, link, picture of each store in foodpanda.com.tw  
&#160; &#160; &#160; &#160;Using request.get() to download the api open data from Food panda, then use json.load() to convert the text to dictionary, so we could get the menu of each store. 
2. Crawling of UberEATS:  
&#160; &#160; &#160; UberEATS cannot directly access through some common Web Crawling tools, and the providing API need specific scope authorization to get the data of stores and menu, needed the complete project plan and days of process time to access the token.  
&#160; &#160; &#160;Therefore, we observed the Developers Console and find the corresponding package then donald it. Using python to decode the json file and get the store's menu information, and then build the formatted data to store in Google Sheet.  
### 2.PyWeb I/O:
&#160; &#160; &#160; &#160;To build an interactive website, we use PyWebIO to get user's information and output the lists and buttons that user can see and click to get to the next step.
1. Image  
&#160; &#160; &#160; &#160;We use the function "put_image" to output our logo and the store image.  
2. Connection with Google Sheet  
&#160; &#160; &#160; &#160; We use Google Sheet as data base, so we need a way to connect our website and the database. We use request function to get the json in Google Sheet , then use the API previously build in Google Sheet, we can access full data about stores, products, even UberEATS and Food panda’s Website URL. 
3. Website design  
&#160; &#160; &#160; &#160; Combine python container and, store datas from database, and the object from PyWeb I/O, we create a recommendation store list according to the time of the day and the tendency of diet. In the store page is the menu from UberEATS and Food panda website, and the respectively price, user can choose the meal they want to order, the program will automatically calculate the total price from each store, then recommend the better store to user.
4. Healthcare  
&#160; &#160; &#160; &#160; Beside comparing total price, we also offer the function to record each order you make, then store in the Google Sheet database. Then according to the order history, we can know if user have order to many drink, supper or fried food, then give the warning
### 3.Google Sheet:
&#160; &#160; &#160; &#160; We save our data in google sheets, open the google sheets to the Internet, then EATAGO can access the database .The history of food ordering is also saved in google sheets. 

## How to use Eatago 
### 1. Select Your Name
&#160; &#160; &#160; &#160;Eatago,a personal life manager, only works when it knows who is using the website. In this case, everyone will have their own Eatago and know precisely what they have had.
### 2. Select Mode
&#160; &#160; &#160; &#160;Though it is beneficial for us eat healthy. It is impossible to eat same kinds of food daily; hence, there are three modes for users to select. People will get different list of menu including different stores. Normal 
mode enables the user access every store while healthy mode banned junk foods and overeating mode will be filled with junk foods.
### 3. Choose Prefer Store
&#160; &#160; &#160; &#160;The list of stores will be shown after selecting modes, enabling us to hit the button of the store we are fond of.
### 4. Decide Our Order
&#160; &#160; &#160; &#160;Entering the page of the chosen store, we can click the food we tend to have and key in the number we want. The sum of the money will be calculated promptly, telling us which platform is the butter. Of course, if the meal chooses were offered on only one platform, the very one will be the recommended one regardless of the number of money. The url of the store on both website will be given. Lastly, hit submit and the data will be stored ,helping Eatago know better of our diet.
### 5. Take a Look at the Records
&#160; &#160; &#160; &#160;Hit 'F5' or refresh, which will bring us back to Step2. We can then see the record is updated with our latest order. The time we ordered ,the name of the store, and what we have ordered will all be in the document.
It will then enables Eatago notify us whether we are on a healthy diet.
## Future Outlook
###     1. Connection with Food panda and UberEATS
&#160; &#160; &#160; &#160;Although Eatago have the function to place orders, users still have to connect to the website of Food panda or UberEATS. We plan to improve Eatago making it able to help users placing orders directly through our website. We will also hope to cooperate with banks and make it possible to use credit cards to reach the goal of avoiding contacting.
###    2. The Combination of Other Database
&#160; &#160; &#160; &#160;We plan to make a database including the nutrient content and calories of all the foods. Getting the information of the health of the user, Eatago will calculate  that how much amount of nutrients and calories the user should ingest every day and every meal. Eatgo will also recommend foods that fit the needs to ensure that people eat in a healthy way.
###    3. A System that Saves Time
&#160; &#160; &#160; &#160;An extra system about delivering time will be found to lessen the waiting time or our staving time. The system will record when we order food everyday and infer the time we will be hungry, notifying us to order in advance. If we forget to order earlier, the system will also find and show the store that can offer food the fastest and the delivering time is the shortest. With the system mentioned, we can be free from starving.
###    4. Andvanced Group Order
&#160; &#160; &#160; &#160;After the threat of Covid-19, when it is save for people to contact with each other, Eatago will have the option of making Advanced group order. Eatago will timely shows how many people around you are viewing the foods of same store, and make it possible to make a group order with strangers nearby. In this case, we can save the delivery fee and make it more environmental to order foods since it only needs one drive to satisfy the need of many people, which saves oil and lessen the emission of Greenhouse gas. 

## Others: Why Eatago
&#160; &#160; &#160; &#160;As a student of NCTU, the college that use Food Panda the most frequently, usually spend a lot of money on those platforms. Every time we will open two apps and compare the foods, which is really inconvenient to us. It is the inconvenience that inspires us to make Eatago.

