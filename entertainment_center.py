import media
import fresh_tomatoes

"""

    Lists all categories to be utilized on the website:

    title
    release_year
    MPAA rating
    runtime
    genre
    rotten tomatoes score
    synopsis
    poster image url
    youtube trailer url

"""


tropic_thunder = media.Movie(   'Tropic Thunder',
                                '2008',
                                'R',
                                '1h 47min',
                                'Comedy',
                                '82%',
                                'Tugg Speedman (Ben Stiller), pampered action superstar, sets out for Southeast Asia to take part in the biggest, \
                                most-expensive war movie produced, but soon after filming begins, he and his co-stars, \
                                Oscar-winner Kirk Lazarus (Robert Downey Jr.), comic Jeff Portnoy (Jack Black) and the rest of the crew, \
                                must become real soldiers when fighting breaks out in that part of the jungle.',
                                'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_SY1000_CR0,0,711,1000_AL_.jpg',
                                'https://youtu.be/T-6YhRZowgc')


senna = media.Movie('Senna',
                    '2010',
                    'PG-13',
                    '1h 46min',
                    'Documentary',
                    '92%',
                    "Senna is a 2010 British documentary that depicts the life and death of Brazilian motor-racing champion Ayrton Senna, \
                    directed by Asif Kapadia. The film's narrative focuses on Senna's racing career in Formula One, \
                    from his debut in the 1984 Brazilian Grand Prix to his death in an accident at the 1994 San Marino Grand Prix, \
                    with particular emphasis on his rivalry with fellow driver Alain Prost. \
                    It relies primarily on archive racetrack footage and home video clips provided by the Senna family, \
                    rather than retrospective video interviews, and has no formal commentary.",
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MTUzOTAxMl5BMl5BanBnXkFtZTcwODQzMjg3NA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    'https://youtu.be/QOQLeqRcgKc')


john_wick = media.Movie('John Wick',
                        '2014',
                        'R',
                        '1h 41min',
                        'Action',
                        '85%',
                        "Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. \
                        Her sudden death leaves John in deep mourning. \
                        When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car \
                        and kill the puppy that was a last gift from his wife, \
                        John unleashes the remorseless killing machine within and seeks vengeance. \
                        Meanwhile, Iosef's father (Michael Nyqvist) -- John's former colleague -- puts a huge bounty on John's head.",
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
                        'https://youtu.be/2AUmvWm5ZDQ')


deadpool = media.Movie( 'Deadpool',
                        '2016',
                        'R',
                        '1h 48min',
                        'Action',
                        '84%',
                        'Wade Wilson (Ryan Reynolds) is a former Special Forces operator who now works as a mercenary. \
                        His world comes crashing down when evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms him into Deadpool. \
                        The rogue experiment leaves Deadpool with accelerated healing powers and a twisted sense of humor. \
                        With help from mutant allies Colossus and Negasonic Teenage Warhead (Brianna Hildebrand), \
                        Deadpool uses his new skills to hunt down the man who nearly destroyed his life.',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg',
                        'https://youtu.be/Z5ezsReZcxU')


zoolander = media.Movie('Zoolander',
                        '2001',
                        'PG-13',
                        '1h 30min',
                        'Comedy',
                        '64%',
                        "Propelled to the top of the fashion world by a photogenic gaze he calls Blue Steel, \
                        dimwitted male model Derek Zoolander (Ben Stiller) thinks he's got a fourth consecutive win as \
                        Male Model of the Year in the bag. But, when his rival, Hansel (Owen Wilson), unexpectedly takes the crown, \
                        Derek is crushed. He becomes easy prey for fashion designer Jacobim Mugatu (Will Ferrell), \
                        who signs Derek to star in his Derelicte fashion show, then brainwashes him to kill Malaysia's prime minister.",
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEwOTMxMDE@._V1_.jpg',
                        'https://youtu.be/YtQq0T3ExLs')


the_interview = media.Movie('The Interview',
                            '2014',
                            'R',
                            '1h 52min',
                            'Comedy',
                            '52%',
                            "Dave Skylark (James Franco) and his producer Aaron Rapoport (Seth Rogen) \
                            are the team behind the popular tabloid-TV show Skylark Tonight. \
                            After learning that North Korea's Kim Jong Un (Randall Park) is a huge fan of the show, \
                            they successfully set up an interview with him, hoping to legitimize themselves as actual journalists. \
                            However, as Dave and Aaron prepare for their journey to Pyongyang, the CIA steps in, \
                            recruits them, and assigns them an incredible mission: Assassinate the dictator.",
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQzMTcwMzgyMV5BMl5BanBnXkFtZTgwMzAyMzQ2MzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                            'https://youtu.be/kP8O-MOqmcw')



kung_fury = media.Movie("Kung Fury",
                        "2015",
                        "NR",
                        "31min",
                        "Action",
                        "86%",
                        "Kung Fury is a 2015 English-language Swedish martial arts action comedy short film written, \
                        directed by, and starring David Sandberg. \
                        It pays homage to 1980s martial arts and police action films. \
                        In it, a kung-fu cop (David Sandberg) travels back in time to kill Adolf Hitler.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwMjU2ODU5NF5BMl5BanBnXkFtZTgwNTU1NjM4NTE@._V1_SY999_CR0,0,702,999_AL_.jpg",
                        "https://youtu.be/bS5P_LAqiVg")

pacific_rim = media.Movie(  "Pacific Rim",
                            "2013",
                            "PG-13",
                            "2h 11min",
                            "Action",
                            "71%",
                            "Long ago, legions of monstrous creatures called Kaiju arose from the sea, \
                            bringing with them all-consuming war. To fight the Kaiju, \
                            mankind developed giant robots called Jaegers, \
                            designed to be piloted by two humans locked together in a neural bridge. \
                            However, even the Jaegers are not enough to defeat the Kaiju, \
                            and humanity is on the verge of defeat. Mankind's last hope now lies with \
                            a washed-up ex-pilot (Charlie Hunnam), an untested trainee (Rinko Kikuchi) and an old, obsolete Jaeger.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZTcwOTU1OTU0OQ@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                            "https://youtu.be/5guMumPFBag")

airplane = media.Movie(     "Airplane!",
                            "1980",
                            "PG",
                            "1h 28min",
                            "Comedy",
                            "97%",
                            "This spoof comedy takes shots at the slew of disaster movies that were released in the 70s. \
                            When the passengers and crew of a jet are incapacitated due to food poisoning, \
                            a rogue pilot, afraid to fly, with a drinking problem must cooperate with his \
                            ex-girlfriend turned stewardess to bring the plane to a safe landing.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNDU2MjE4MTcwNl5BMl5BanBnXkFtZTgwNDExOTMxMDE@._V1_.jpg",
                            "https://youtu.be/HMnVs287AJ4")

#########################
#         Anime         #
#########################




#########################
#           TV          #
#########################



movies = [tropic_thunder, senna, airplane, john_wick, deadpool, the_interview, zoolander, pacific_rim, kung_fury]
fresh_tomatoes.open_movies_page(movies)
