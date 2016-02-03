from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///phillyrestaurants.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

restaurant1 = Restaurant(user_id=1,
                         name="Hawthornes Biercafe",
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzOXJrR05tMFdrR1U',
                         interior='https://drive.google.com/open?id=0B0AV8BnWCTfzOTZjTDMzWHNCbDQ',
                         link='http://www.hawthornecafe.com/',
                         neighborhood='Bella Vista',
                         street='738 S. 11th Street',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19147',
                         foodtype='American')

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1,
                     name="Carolina Shrimp & Grits",
                     description="Jumbo shrimp, smoked bacon, bell peppers, scallions, roasted tomatoes, sharp cheddar grits, pork fat jus",
                     price="$17.00",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,
                     name="Warm Cracked Grain Salad",
                     description="Roasted mushrooms & eggplant, farro, lentils, quinoa, feta, baby spinach, charred onion balsamic vinaigrette",
                     price="$13.00",
                     course="Appetizer",
                     restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,
                     name="Fried Chicken & Waffles",
                     description="Homemade Buttermilk Waffle Topped with Boneless Skin on Chicken Thighs Fried to a Crispy Perfection, Two Poached Eggs, Hollandaise and Mixed Greens",
                     price="$14.00",
                     course="Brunch",
                     restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,
                     name="South of The Border",
                     description="Two Crispy Corn Tortillas, Topped with Two Over Easy Eggs, Black Bean Salad, Sharp Cheddar, Avocado, Spicy Ranchero, Cilantro Sour Cream & Scallion, Homefries",
                     price="$12.00",
                     course="Brunch",
                     restaurant=restaurant1)

session.add(menuItem4)
session.commit()

restaurant2 = Restaurant(user_id=1,
                         name='Miles Table',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzZXVLQS1iX0lpWjg',
                         interior='http://cdn-jpg.thedailymeal.net/sites/default/files/user_img_uploads/u45592/rsz_miles_table_2.jpg',
                         link='http://milestable.com/',
                         neighborhood='Graduate Hospital',
                         street='1620 South Street',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19146',
                         foodtype='American')

session.add(restaurant2)
session.commit()

menuItem5 = MenuItem(user_id=1,
                     name="Thai Crispy Chicken",
                     description="Fried half chicken, sambal chili, steamed rice, charred scallions",
                     price="$16.00",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,
                     name="Crispy Cauliflower",
                     description="Sambal chili sauce, scallions, peppers, onions, sesame seeds",
                     price="$7.00",
                     course="Appetizer",
                     restaurant=restaurant2)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,
                     name="Turkey Burger",
                     description="Fresh ground with cheddar, chipotle mayo",
                     price="$11.00 ($5.50 on Wednesdays)",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1,
                     name="Eggplant Parmesan",
                     description="Crispy eggplant, arugula, mushrooms, basil marinara, mozzarella, greens",
                     price="$15.00",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem8)
session.commit()

restaurant3 = Restaurant(user_id=1,
                         name='Khyber Pass',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzMF84MFBvazZ0VUE',
                         interior='http://cdn.phillymag.com/wp-content/uploads/2011/10/contents_d5-1024x571.jpg',
                         link='http://www.khyberpasspub.com/',
                         neighborhood='Old City',
                         street='56 S 2nd St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19106',
                         foodtype='Cajun')

session.add(restaurant3)
session.commit()

menuItem9 = MenuItem(user_id=1,
                     name="Khyber Gumbo",
                     description="chicken, Best Stop's andouille sausage",
                     price="cup $5.50 bowl $8.00",
                     course="Appetizer",
                     restaurant=restaurant3)

session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(user_id=1,
                      name="Fried Shrimp Po-boy",
                      description="Leidenheimer roll, dressed with lettuce, tomato, pickles, mayo",
                      price="$17.00",
                      course="Entree",
                      restaurant=restaurant3)

session.add(menuItem10)
session.commit()

menuItem11 = MenuItem(user_id=1,
                      name="North Carolina-style BBQ Pulled Pork",
                      description="spicy vinegar barbecue sauce, coleslaw",
                      price="$12.00",
                      course="Entree",
                      restaurant=restaurant3)

session.add(menuItem11)
session.commit()

menuItem12 = MenuItem(user_id=1,
                      name="Grilled Vegan Sausage",
                      description="our seitan sausage patties, lettuce, roasted poblanos, red onion, pickles, creole mustard, vegan mayo",
                      price="$13.00",
                      course="Entree",
                      restaurant=restaurant3)

session.add(menuItem12)
session.commit()

restaurant4 = Restaurant(user_id=1,
                         name='The Dandelion Pub',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzc0k3R3luUk81a0U',
                         interior='http://media.philly.com/images/600*450/aerick16-zz.jpg',
                         link='http://thedandelionpub.com/',
                         neighborhood='Rittenhouse',
                         street='124 S 18th St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19103',
                         foodtype='British')

session.add(restaurant4)
session.commit()

menuItem13 = MenuItem(user_id=1,
                      name="Butter Lettuce Salad",
                      description="honey crisp apples, pomegranate seeds, spiced walnuts, tuxford & tebbutt stilton, honey vinaigrette",
                      price="$10.50",
                      course="Appetizer",
                      restaurant=restaurant4)

session.add(menuItem13)
session.commit()

menuItem14 = MenuItem(user_id=1,
                      name="Beer-Battered Fish & Chips",
                      description="line-caught cod, tartar sauce, triple cooked chips",
                      price="$19.75",
                      course="Entree",
                      restaurant=restaurant4)

session.add(menuItem14)
session.commit()

menuItem15 = MenuItem(user_id=1,
                      name="Crab Risotto",
                      description="zucchini, charred leeks, lemon gremolata, saffron, chilies",
                      price="$15.00",
                      course="Entree",
                      restaurant=restaurant4)

session.add(menuItem15)
session.commit()

menuItem16 = MenuItem(user_id=1,
                      name="Duck Bolognese",
                      description="sunny side duck egg, strozzapreti pasta",
                      price="$19.50",
                      course="Entree",
                      restaurant=restaurant4)

session.add(menuItem16)
session.commit()

restaurant5 = Restaurant(user_id=1,
                         name='Fat Ham',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzSGJVYmNaMVdMN0k',
                         interior='http://cdn.cstatic.net/images/gridfs/52a23146f92ea1695900a143/fatham7.jpg',
                         link='https://www.sbragadining.com/fatham/',
                         neighborhood='University City',
                         street='3131 Walnut St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19104',
                         foodtype='Southern')

session.add(restaurant5)
session.commit()

menuItem17 = MenuItem(user_id=1,
                      name="Skillet Cornbread",
                      description="tasso, molasses butter, fine herbs",
                      price="$8.00",
                      course="Appetizer",
                      restaurant=restaurant5)

session.add(menuItem17)
session.commit()

menuItem18 = MenuItem(user_id=1,
                      name="Grilled Beets",
                      description="fennel lemon dressing, pickled beets",
                      price="$6.00",
                      course="Appetizer",
                      restaurant=restaurant5)

session.add(menuItem18)
session.commit()

menuItem19 = MenuItem(user_id=1,
                      name="Shrimp & Grits",
                      description="country ham, scallion, peanuts",
                      price="$15.00",
                      course="Entree",
                      restaurant=restaurant5)

session.add(menuItem19)
session.commit()

menuItem20 = MenuItem(user_id=1,
                      name="Hot Chicken",
                      description="brioche, ranch dressing, dill pickles",
                      price="$15.00",
                      course="Entree",
                      restaurant=restaurant5)

session.add(menuItem20)
session.commit()

restaurant6 = Restaurant(user_id=1,
                         name='La Viola: Ovest',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzcWVTQjdZeUNES1U',
                         interior='http://laviolaphiladelphia.com/assets/west/events/photo03.png',
                         link='http://laviolaphiladelphia.com/west/',
                         neighborhood='Rittenhouse',
                         street='253 S 16th St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19102',
                         foodtype='Italian')

session.add(restaurant6)
session.commit()

menuItem21 = MenuItem(user_id=1,
                      name="Frutti Di Mare Alla Griglia",
                      description="grilled calamari and shrimp marinated in a lemon juice, garlic and peppered olive oil sauce",
                      price="$9.00",
                      course="Appetizer",
                      restaurant=restaurant6)

session.add(menuItem21)
session.commit()

menuItem22 = MenuItem(user_id=1,
                      name="Pollo Alla Fontina",
                      description="chicken breast topped with asparagus, prosciutto di parma and fontina cheese in a light marinara sauce",
                      price="$16.00",
                      course="Entree",
                      restaurant=restaurant6)

session.add(menuItem22)
session.commit()

menuItem23 = MenuItem(user_id=1,
                      name="Vitello Rollatini",
                      description="veal medallions stuffed with spinach, smoked ham and fontina cheese in a rosee sauce with mushrooms and chopped tomatoes",
                      price="$18.00",
                      course="Entree",
                      restaurant=restaurant6)

session.add(menuItem23)
session.commit()

menuItem24 = MenuItem(user_id=1,
                      name="Orecchiette Alla Viola",
                      description="shell shaped pasta tossed with veal sausage, chicken and mushrooms in a white wine sauce with fresh tomatoes",
                      price="$16.00",
                      course="Entree",
                      restaurant=restaurant6)

session.add(menuItem24)
session.commit()

restaurant7 = Restaurant(user_id=1,
                         name='Amada',
                         logo='http://philadelphia.amadarestaurant.com/a/i/logo-print.png',
                         interior='http://philadelphia.amadarestaurant.com/m/widgets/PDR1436x650.jpg',
                         link='http://philadelphia.amadarestaurant.com/',
                         neighborhood='Old City',
                         street='217 Chestnut St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19106',
                         foodtype='Spanish')

session.add(restaurant7)
session.commit()

menuItem25 = MenuItem(user_id=1,
                      name="Sopa De Pataca",
                      description="sunchoke soup, duck confit, cherry espuma, rosemary",
                      price="$13.00",
                      course="Appetizer",
                      restaurant=restaurant7)

session.add(menuItem25)
session.commit()

menuItem26 = MenuItem(user_id=1,
                      name="Costillas De Ternera",
                      description="flatbread with beef short ribs, horseradish, parmesan, bacon",
                      price="$14.00",
                      course="Entree",
                      restaurant=restaurant7)

session.add(menuItem26)
session.commit()

menuItem27 = MenuItem(user_id=1,
                      name="Fideos Con Mariscos",
                      description="calamari linguine & vermicelli, clams, diver scallops, sweet onion cream",
                      price="$18.00",
                      course="Entree",
                      restaurant=restaurant7)

session.add(menuItem27)
session.commit()

menuItem28 = MenuItem(user_id=1,
                      name="Gambas Al Ajillo",
                      description="garlic shrimp",
                      price="$10.00",
                      course="Appetizer",
                      restaurant=restaurant7)

session.add(menuItem28)
session.commit()

restaurant8 = Restaurant(user_id=1,
                         name='My Thai',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzMHpkb0pjaVl0aFk',
                         interior='http://s3-media1.fl.yelpcdn.com/bphoto/izdQFg675LeOPj0-fVHaMA/o.jpg',
                         link='',
                         neighborhood='Graduate Hospital',
                         street='2200 South St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19146',
                         foodtype='Thai')

session.add(restaurant8)
session.commit()

menuItem29 = MenuItem(user_id=1,
                      name="Tom Kha Gai",
                      description="chicken coconut soup. chicken soup in coconut milk with lemongrass, galanka, lime leaves, bell peppers and scallions",
                      price="$4.50",
                      course="Appetizer",
                      restaurant=restaurant8)

session.add(menuItem29)
session.commit()

menuItem30 = MenuItem(user_id=1,
                      name="Phad Thai",
                      description="ever popular thai rice noodle with shrimp, tofu, scallions bean sprouts sauteed with egg and ground peanut",
                      price="$12.50",
                      course="Entree",
                      restaurant=restaurant8)

session.add(menuItem30)
session.commit()

menuItem31 = MenuItem(user_id=1,
                      name="Panang Shrimp",
                      description="shrimp sauteed with spicy peanut, lime leaf, coconut curry sauce",
                      price="$15.00",
                      course="Entree",
                      restaurant=restaurant8)

session.add(menuItem31)
session.commit()

menuItem32 = MenuItem(user_id=1,
                      name="Gang Ped",
                      description="thai curry pot. choice sliced chicken or beef with red curry, coconut milk, eggplants and bamboo shoots",
                      price="$13.00",
                      course="Entree",
                      restaurant=restaurant8)

session.add(menuItem32)
session.commit()

restaurant9 = Restaurant(user_id=1,
                         name='El Rey',
                         logo='https://drive.google.com/open?id=0B0AV8BnWCTfzNUpBSlJ4eWRhWkU',
                         interior='http://media.philly.com/images/20100422_inq_table22z-b.JPG',
                         link='http://www.elreyrestaurant.com/',
                         neighborhood='Rittenhouse',
                         street='2013 Chestnut St',
                         city='Philadelphia',
                         state='PA',
                         zipcode='19103',
                         foodtype='Mexican')

session.add(restaurant9)
session.commit()

menuItem29 = MenuItem(user_id=1,
                      name="Sopa De Hongos",
                      description="wild mushroom soup",
                      price="$5.50",
                      course="Appetizer",
                      restaurant=restaurant9)

session.add(menuItem29)
session.commit()

menuItem30 = MenuItem(user_id=1,
                      name="Camarones",
                      description="shrimp, fried garlic, squeeze of lime",
                      price="$15.50",
                      course="Entree",
                      restaurant=restaurant9)

session.add(menuItem30)
session.commit()

menuItem31 = MenuItem(user_id=1,
                      name="Zarape",
                      description="steak and fried potatoes between 2 crispy tortillas smothered in arbol salsa topped with pasilla peppers , fried duck egg, and crema",
                      price="$13.00",
                      course="Entree",
                      restaurant=restaurant9)

session.add(menuItem31)
session.commit()

menuItem32 = MenuItem(user_id=1,
                      name="Campachi Ceviche",
                      description="campachi, radish, apple, tomato, jalapeno with orange and avocado topped with fried jicama & red onion",
                      price="$12.00",
                      course="Entree",
                      restaurant=restaurant9)

session.add(menuItem32)
session.commit()

restaurant10 = Restaurant(user_id=1,
                          name='Tio Flores',
                          logo='https://drive.google.com/open?id=0B0AV8BnWCTfzQUhYaFdheEc3ZDA',
                          interior='https://pbs.twimg.com/media/CTZExiRWEAEhhgx.png',
                          link='http://www.tioflores.com/',
                          neighborhood='Graduate Hospital',
                          street='1600 South St',
                          city='Philadelphia',
                          state='PA',
                          zipcode='19146',
                          foodtype='Mexican')

session.add(restaurant10)
session.commit()

menuItem29 = MenuItem(user_id=1,
                      name="Lentil & Cauliflower Tacos [2]",
                      description="lentils, roasted cauliflower, queso fresco, warmed pico de gallo, lime crema ",
                      price="$10.00",
                      course="Appetizer",
                      restaurant=restaurant10)

session.add(menuItem29)
session.commit()

menuItem30 = MenuItem(user_id=1,
                      name="Tequila Chipotle Shrimp Tacos [2]",
                      description="avocado, jicama slaw, lime crema",
                      price="$10.00",
                      course="Entree",
                      restaurant=restaurant10)

session.add(menuItem30)
session.commit()

menuItem31 = MenuItem(user_id=1,
                      name="Beer Battered Tilapia Tacos [2]",
                      description="jicama slaw, lime crema",
                      price="$15.00",
                      course="Entree",
                      restaurant=restaurant10)

session.add(menuItem31)
session.commit()

menuItem32 = MenuItem(user_id=1,
                      name="Gringa Tacos [2]",
                      description="chicken tinga, avocado, queso fresco, lime crema, lettuce, chili de arbol ",
                      price="$10.00",
                      course="Entree",
                      restaurant=restaurant10)

session.add(menuItem32)
session.commit()