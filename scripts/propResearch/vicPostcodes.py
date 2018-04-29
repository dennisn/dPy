"""
Simple VIC postcode parser
Created on Sun May 01 16:51:38 2016

@author: DennisNguyen
"""

VicPostcodeData='''3000	Melbourne
3001	Melbourne
3002	East Melbourne
3003	West Melbourne
3005	World Trade Centre
3006	Southbank
3008	Docklands
3010	University Of Melbourne
3011	Footscray, Seddon, Seddon West
3012	Brooklyn, Kingsville, Maidstone, Tottenham, West Footscray
3013	Yarraville, Yarraville West
3015	Newport, South Kingsville, Spotswood
3016	Williamstown
3018	Altona, Seaholme
3019	Braybrook, Robinson
3020	Albion, Sunshine
3021	Albanvale, Kealba, Kings Park, St Albans
3022	Ardeer, Deer Park East
3023	Burnside, Cairnlea, Caroline Springs, Deer Park
3024	Mount Cottrell, Wyndham Vale
3025	Altona North
3026	Laverton North
3028	Altona Meadows, Laverton, Seabrook
3029	Hoppers Crossing, Tarneit, Truganina
3030	Derrimut, Point Cook, Werribee
3031	Flemington, Kensington
3032	Ascot Vale, Highpoint City, Maribyrnong, Travancore
3033	East Keilor
3034	Avondale Heights
3036	Keilor, Keilor North
3037	Delahey, Hillside, Sydenham
3038	Keilor Downs, Taylors Lakes
3039	Moonee Ponds
3040	Aberfeldie, Essendon, Essendon West
3041	Essendon North, Strathmore, Strathmore Heights
3042	Airport West, Keilor Park, Niddrie
3043	Gladstone Park, Gowanbrae, Tullamarine
3044	Pascoe Vale, Pascoe Vale South
3045	Melbourne Airport
3046	Glenroy, Hadfield, Oak Park
3047	Broadmeadows, Dallas, Jacana
3048	Coolaroo, Meadow Heights
3049	Attwood, Westmeadows
3050	Royal Melbourne Hospital
3051	Hotham Hill, North Melbourne
3052	Melbourne University, Parkville
3053	Carlton, Carlton South
3054	Carlton North, Princes Hill
3055	Brunswick West
3056	Brunswick
3057	Brunswick East
3058	Coburg, Coburg North, Merlynston, Moreland
3059	Greenvale
3060	Fawkner
3061	Campbellfield
3062	Somerton
3063	Oaklands Junction, Yuroke
3064	Craigieburn, Donnybrook, Kalkallo, Mickleham, Roxburgh Park
3065	Fitzroy
3066	Collingwood
3067	Abbotsford
3068	Clifton Hill, Fitzroy North
3070	Northcote
3071	Thornbury
3072	Northland Centre, Preston, Preston South, Regent West
3073	Reservoir, Keon Park
3074	Thomastown
3075	Lalor
3076	Epping, Epping Dc
3078	Alphington, Fairfield
3079	Ivanhoe, Ivanhoe East
3081	Heidelberg Heights, Heidelberg Rgh, Heidelberg West
3082	Mill Park
3083	Bundoora, Kingsbury
3084	Banyule, Eaglemont, Heidelberg, Rosanna, Viewbank
3085	Macleod, Yallambie
3087	Watsonia
3088	Briar Hill, Greensborough, Saint Helena
3089	Diamond Creek
3090	Plenty
3091	Yarrambat
3093	Lower Plenty
3094	Montmorency
3095	Eltham, Eltham North, Research
3096	Wattle Glen
3097	Bend Of Islands, Kangaroo Ground, Watsons Creek
3099	Arthurs Creek, Cottles Bridge, Hurstbridge, Nutfield, Strathewen
3101	Kew
3102	Kew East
3103	Balwyn
3104	Balwyn North
3105	Bulleen
3106	Templestowe
3107	Templestowe Lower
3108	Doncaster
3109	Doncaster East, Doncaster Heights, Tunstall Square Po
3110	Nunawading Bc
3111	Donvale
3113	North Warrandyte, Warrandyte
3114	Park Orchards
3115	Wonga Park
3116	Chirnside Park
3121	Burnley, Cremorne, Richmond
3122	Hawthorn
3123	Hawthorn East
3124	Camberwell, Camberwell North, Camberwell South, Camberwell West, Middle Camberwell
3125	Bennettswood, Burwood
3126	Camberwell East, Canterbury
3127	Mont Albert, Surrey Hills
3128	Box Hill, Box Hill South, Houston, Wattle Park
3129	Box Hill North, Kerrimuir, Mont Albert North
3130	Blackburn, Blackburn North, Blackburn South, Laburnum
3131	Brentford Square, Forest Hill, Nunawading
3132	Mitcham, Rangeview
3133	Vermont, Vermont South
3134	Ringwood, Ringwood North, Warrandyte South, Warranwood
3135	Bedford Road, Heathmont, Ringwood East
3136	Croydon, Croydon Hills, Croydon North, Croydon South
3137	Kilsyth, Kilsyth South
3138	Mooroolbark
3139	Hoddles Creek, Launching Place, Seville, Wandin North, Woori Yallock, Yellingbo
3140	Lilydale
3141	South Yarra
3142	Hawksburn, Toorak
3143	Armadale, Armadale North
3144	Kooyong, Malvern
3145	Caulfield East, Central Park, Darling, Malvern East
3146	Glen Iris
3147	Ashburton, Ashwood
3148	Chadstone, Holmesglen
3149	Mount Waverley, Syndal
3150	Glen Waverley, Wheelers Hill
3151	Burwood East, Burwood Heights
3152	Knox City Centre, Studfield, Wantirna, Wantirna South
3153	Bayswater, Bayswater North
3154	The Basin
3155	Boronia
3156	Ferntree Gully, Lysterfield, Lysterfield South, Mountain Gate, Upper Ferntree Gully
3158	Upwey
3159	Menzies Creek, Selby
3160	Belgrave, Tecoma
3161	Caulfield Junction, Caulfield North
3162	Caulfield, Caulfield South, Hopetoun Gardens
3163	Carnegie, Glen Huntly, Murrumbeena
3164	Dandenong South
3165	Bentleigh East, Coatesville
3166	Hughesdale, Huntingdale, Oakleigh, Oakleigh East
3167	Oakleigh South
3168	Clayton, Notting Hill
3169	Clarinda, Clayton South
3170	Mulgrave
3171	Sandown Village, Springvale
3172	Dingley Village, Springvale South
3173	Keysborough
3174	Noble Park, Noble Park North
3175	Bangholme, Dandenong, Dandenong North, Dandenong South
3176	Scoresby Bc
3177	Doveton, Eumemmerring
3178	Rowville
3179	Scoresby
3180	Knoxfield
3181	Prahran, Windsor
3182	St Kilda, St Kilda South, St Kilda West
3183	Balaclava, St Kilda East
3184	Brighton Road, Elwood
3185	Elsternwick, Gardenvale, Ripponlea
3186	Brighton, Dendy
3187	Brighton East, North Road
3188	Hampton, Hampton East, Hampton North
3189	Moorabbin, Moorabbin East, Wishart
3190	Highett
3191	Sandringham
3192	Cheltenham, Cheltenham East, Southland Centre
3193	Beaumaris, Black Rock, Cromer
3194	Mentone, Moorabbin Airport
3195	Aspendale, Aspendale Gardens, Braeside, Mordialloc, Parkdale, Waterways
3196	Bonbeach, Chelsea, Chelsea Heights, Edithvale
3197	Carrum, Patterson Lakes
3198	Belvedere Park, Seaford
3199	Frankston, Frankston South, Karingal
3200	Frankston North, Pines Forest
3201	Carrum Downs
3202	Heatherton
3204	Bentleigh, Mckinnon, Ormond
3205	South Melbourne, South Melbourne Dc
3206	Albert Park, Middle Park
3207	Garden City, Port Melbourne
3211	Little River
3212	Lara
3214	Corio, Norlane, North Shore
3215	Bell Park, Bell Post Hill, Hamlyn Heights, North Geelong
3216	Belmont, Freshwater Creek, Grovedale, Highton, Marshall, Mount Duneed, Wandana Heights, Waurn Ponds
3217	Deakin University
3218	Geelong West, Herne Hill, Manifold Heights
3219	Breakwater, East Geelong, Newcomb, St Albans Park, Whittington
3220	Geelong, Newtown
3221	Anakie, Barrabool, Batesford, Bellarine, Ceres, Fyansford, Gnarwarre, Kennett River, Lovely Banks, Moolap, Moorabool, Murgheboluc, Staughton Vale, Stonehaven, Wallington, Wongarra, Wye River
3222	Clifton Springs, Curlewis, Drysdale, Mannerim, Marcus Hill
3223	Indented Head, Portarlington, St Leonards
3224	Leopold
3225	Point Lonsdale, Queenscliff
3226	Ocean Grove
3227	Barwon Heads, Breamlea, Connewarre
3228	Bellbrae, Jan Juc, Torquay
3230	Anglesea
3231	Aireys Inlet, Eastern View, Fairhaven, Moggs Creek
3232	Lorne
3233	Apollo Bay, Skenes Creek
3235	Deans Marsh
3236	Forrest
3237	Beech Forest, Gellibrand Lower
3238	Hordern Vale, Johanna
3239	Carlisle River, Chapple Vale, Gellibrand, Kennedys Creek
3240	Buckley, Modewarre, Moriac, Mount Moriac
3241	Bambra, Winchelsea, Wurdiboluc
3242	Birregurra
3243	Barwon Downs, Gerangamete, Murroon, Warncoort
3249	Alvie, Barongarook, Barramunga, Coragulac, Corunnun, Dreeite, Irrewarra, Kawarren, Larpent, Nalangil, Ondit, Pirron Yallock, Swan Marsh, Warrion, Wool Wool, Yeo, Yeodene
3250	Colac, Elliminyt
3251	Beeac, Cundare North, Weering
3254	Cororooke
3260	Bungador, Camperdown, Gnotuk, Pomborneit, Stonyford
3264	Terang
3265	Boorcan, Ellerslie, Garvoc, Kolora, Noorat, Panmure, The Sisters
3266	Cobden, Glenfyne, Jancourt, Jancourt East, Simpson
3267	Scotts Creek
3268	Curdie Vale, Curdies River, Nirranda, Nullawarre, Timboon
3269	Port Campbell, Princetown
3270	Peterborough
3271	Darlington, Dundonnell, Pura Pura
3272	Mortlake, Woorndoo
3273	Hexham
3274	Caramut
3275	Mailer Flat
3276	Woolsthorpe
3277	Allansford, Mepunga, Naringal
3278	Purnim
3279	Wangoom
3280	Dennington, Warrnambool
3281	Bushfield, Grassmere, Winslow, Woodford
3282	Illowa, Koroit
3283	Killarney, Kirkstall, Southern Cross, Tower Hill
3284	Port Fairy
3285	Narrawong, Rosebrook, St Helens, Toolong, Tyrendarra, Yambuk
3286	Macarthur
3287	Hawkesdale, Minhamite
3289	Penshurst
3292	Nelson
3293	Glenthompson
3294	Dunkeld, Moutajup, Victoria Valley
3300	Hamilton
3301	Broadwater, Byaduk, Strathkellar, Tarrington
3302	Branxholme
3303	Condah
3304	Dartmoor, Heywood, Winnap
3305	Allestree, Bolwarra, Gorae, Portland
3309	Digby
3310	Merino
3311	Casterton
3312	Carapook, Chetwynd, Dergholm, Henty, Lake Mundi, Poolaijelo, Sandford, Strathdownie, Wando Vale
3314	Cavendish
3315	Coleraine, Melville Forest, Nareen
3317	Harrow
3318	Connewirricoo, Edenhope, Langkoop
3319	Apsley, Benayeo
3321	Inverleigh
3322	Cressy
3323	Berrybank, Duverney
3324	Lismore
3325	Derrinallum
3328	Teesdale
3329	Barunah Park, Shelford
3330	Rokewood
3331	Bannockburn, Gheringhap, Maude, Russells Bridge, She Oaks, Steiglitz, Sutherlands Creek
3332	Lethbridge
3333	Meredith
3334	Elaine, Morrisons
3335	Rockbank
3337	Kurunjang, Melton, Toolern Vale
3338	Brookfield, Exford, Melton South
3340	Bacchus Marsh, Balliang, Coimadai, Glenmore, Parwan, Rowsley
3341	Greendale, Myrniong
3342	Ballan, Beremboke, Blakeville, Mount Wallace
3345	Gordon
3350	Alfredton, Ballarat, Ballarat North, Ballarat West, Black Hill, Brown Hill, Canadian, Eureka, Golden Point, Lake Wendouree, Mount Clear, Mount Helen, Mount Pleasant, Nerrina, Redan, Sovereign Hill
3351	Berringa, Cape Clear, Carngham, Chepstowe, Haddon, Hillcrest, Illabarook, Lake Bolac, Mininera, Nerrin Nerrin, Rokewood Junction, Ross Creek, Scarsdale, Smythes Creek, Smythesdale, Snake Valley, Streatham, Westmere
3352	Addington, Barkstead, Blowhard, Bolwarrah, Bullarook, Bungaree, Burrumbeet, Cambrian Hill, Cardigan, Clarendon, Clarkes Hill, Corindhap, Dean, Dunnstown, Durham Lead, Enfield, Invermay, Lal Lal, Learmonth, Leigh Creek, Lexton, Magpie, Millbrook, Miners Rest, Mitchell Park, Mollongghip, Mount Egerton, Mount Rowan, Napoleons, Navigators, Pootilla, Scotsburn, Springbank, Wallace, Warrenheip, Waubra, Weatherboard, Werneth, Windermere, Yendon
3353	Ballarat
3354	Bakery Hill, Ballarat Mc
3355	Mitchell Park, Wendouree, Wendouree Village
3356	Delacombe, Sebastopol
3357	Buninyong
3360	Linton
3361	Carranballac, Skipton
3363	Creswick
3364	Allendale, Ascot, Blampied, Broomfield, Campbelltown, Coghills Creek, Kingston, Newlyn, Rocklyn, Smeaton, Ullina
3370	Clunes
3371	Evansford, Stony Creek, Talbot
3373	Beaufort, Trawalla
3375	Bayindeen, Buangor
3377	Ararat, Crowlands, Great Western, Maroona, Mount Lonarch, Moyston, Warrak
3378	Tatyoon
3379	Chatsworth, Stavely, Wickliffe
3380	Stawell
3381	Barkly, Campbells Bridge, Halls Gap, Lubeck, Pomonal
3384	Landsborough, Navarre
3385	Dadswells Bridge, Glenorchy
3387	Marnoo
3388	Banyena, Rupanyup
3390	Murtoa
3391	Brim
3392	Minyip, Sheep Hills
3393	Warracknabeal
3395	Beulah
3396	Hopetoun
3400	Horsham
3401	Dooen, Douglas, Gymbowen, Karnak, Mitre, Noradjuha, Quantong, Rocklands, Telangatuk East, Toolondo, Wallup, Wombelano
3402	Horsham
3407	Balmoral, Gatum, Vasey
3409	Natimuk
3412	Goroke
3413	Minimay, Neuarpurr, Ozenkadnook, Peronne
3414	Antwerp, Dimboola
3415	Lawloit, Miram
3418	Gerang Gerung, Kiata, Nhill, Yanac
3419	Kaniva
3420	Lillimur, Serviceton
3423	Jeparit
3424	Rainbow, Yaapeet
3427	Diggers Rest
3428	Bulla
3429	Sunbury
3430	Clarkefield
3431	Riddells Creek
3432	Bolinda
3434	Kerrie, Romsey
3435	Lancefield
3437	Bullengarook, Gisborne
3438	New Gisborne
3440	Macedon
3441	Mount Macedon
3442	Ashbourne, Carlsruhe, Hesket, Newham, Rochford, Woodend
3444	Redesdale, Tylden, Kyneton, Mia Mia
3446	Drummond North, Malmsbury
3447	Taradale
3448	Elphinstone, Metcalfe, Sutton Grange
3450	Castlemaine
3451	Barkers Creek, Campbells Creek, Chewton, Fryerstown, Golden Point, Guildford, Muckleford
3453	Harcourt, Ravenswood
3458	Blackwood, Fern Hill, Lerderderg, Newbury, Trentham
3460	Daylesford
3461	Bullarto, Drummond, Franklinford, Glenlyon, Hepburn Springs, Korweinguboora, Lyonville, Musk, Yandoit
3462	Muckleford South, Newstead
3463	Baringhup, Laanecoorie, Maldon, Shelbourne, Woodstock West
3464	Carisbrook
3465	Alma, Craigie, Daisy Hill, Golden Point, Majorca, Maryborough, Natte Yallock, Rathscar, Simson, Wareek
3467	Avoca
3468	Amphitheatre
3469	Elmhurst
3472	Bet Bet, Betley, Dunolly, Eddington, Goldsborough, Inkerman, Moliagul
3475	Bealiba, Emu, Logan
3478	Moonambel, Redbank, St Arnaud, Stuart Mill
3480	Areegra, Corack, Donald, Litchfield
3482	Watchem
3483	Birchip
3485	Watchupga, Woomelang
3487	Lascelles
3488	Speed
3489	Tempy
3490	Ouyen
3491	Patchewollock
3494	Carwarp, Colignan, Nangiloc
3496	Cardross, Cullulleraine, Meringur, Red Cliffs, Sunnycliffs, Werrimull
3498	Irymple
3500	Mildura
3501	Mildura Centre Plaza, Nichols Point
3502	Mildura
3505	Cabarita, Merbein
3506	Cowangie
3507	Walpeup
3509	Underbool
3512	Murrayville
3515	Marong
3516	Bridgewater On Loddon, Derby, Leichardt
3517	Inglewood, Jarklin, Salisbury West, Serpentine
3518	Berrimal, Borung, Fernihurst, Mysia, Wedderburn
3520	Korong Vale
3521	Pyalong
3522	Tooborac
3523	Costerfield, Heathcote, Knowsley
3525	Charlton, Wychitella
3527	Wycheproof
3529	Nullawil
3530	Culgoa
3531	Berriwillock
3533	Nandaly, Sea Lake
3537	Boort, Gredgwin
3540	Cannie, Quambatook
3542	Lalbert
3544	Ultima, Waitchie
3546	Bolton, Chinkapook, Manangatang
3549	Robinvale
3550	Bendigo, Kennington, Long Gully, North Bendigo, Quarry Hill, Sandhurst East, Spring Gully, Strathdale, Tysons Reef, White Hills
3551	Arnold, Axedale, Eppalock, Epsom, Huntly, Junortoun, Llanelly, Lockwood South, Longlea, Maiden Gully, Mandurang, Newbridge, Strathfieldsaye, Tarnagulla, Toolleen
3552	Bendigo
3554	Bendigo Dc
3555	Golden Square, Kangaroo Flat
3556	California Gully, Campbells Forest, Comet Hill, Eaglehawk, Myers Flat, Sebastian
3557	Barnadown, Fosterville, Goornong
3558	Elmore, Hunter
3559	Colbinabbin, Corop
3561	Bamawm, Rochester, Nanneella
3562	Torrumbarry
3563	Lockington
3564	Echuca, Kanyapella, Patho, Simmie
3565	Kotta
3566	Gunbower
3567	Leitchville, Mincha West
3568	Cohuna
3570	Raywood
3571	Dingee, Tandarra
3572	Milloo, Piavella, Prairie, Tennyson
3573	Calivil, Mitiamo
3575	Mincha, Pyramid Hill, Yarrawalla
3576	Durham Ox
3579	Kerang, Macorna, Murrabit
3580	Koondrook
3581	Lake Charm
3583	Tresco
3584	Lake Boga
3585	Swan Hill
3588	Woorinen South
3589	Woorinen
3590	Beverford
3591	Vinifera
3594	Nyah
3595	Nyah West
3596	Wood Wood
3597	Piangil
3599	Boundary Bend
3607	Tabilk
3608	Bailieston, Goulburn Weir, Graytown, Nagambie, Wahring
3610	Dhurringile, Murchison
3612	Rushworth, Wanalta
3614	Toolamba
3616	Cooma, Gillieston, Harston, Tatura
3617	Byrneside
3618	Merrigum
3619	Kyabram
3620	Kyabram, Lancaster, Wyuna
3621	Koyuga South, Tongala, Yambuna
3622	Koyuga, Strathallan
3623	Stanhope
3624	Girgarre
3629	Ardmona, Coomboona, Mooroopna, Undera
3630	Benarch, Branditt, Caniambo, Colliver, Dunkirk, Shepparton
3631	Arcadia, Cosgrove, Kialla, Kialla East, Kialla West, Lemnos, Pine Lodge, Shepparton East, Tamleugh West
3632	Shepparton
3633	Congupna
3634	Bunbartha, Invergordon South, Katandra, Marungi, Tallygaroopna
3635	Wunghnu
3636	Invergordon, Numurkah
3637	Waaia
3638	Kotupna, Nathalia
3639	Barmah, Picola
3640	Katunga
3641	Strathmerton
3643	Cobram
3644	Cobram, Yarroweyah
3646	Dookie, Yabba North, Youanmite
3647	Dookie College
3649	Katamatite
3658	Broadford, Clonbinane, Hazeldene, Reedy Creek, Strath Creek
3659	Tallarook
3660	Kerrisdale, Seymour, Trawool
3661	Seymour
3662	Puckapunyal Milpo
3663	Mangalore
3664	Avenel
3665	Locksley, Longwood
3666	Balmattum, Creighton, Euroa, Gooram, Kithbrook, Ruffy, Strathbogie
3669	Boho South, Creek Junction, Gowangardie, Koonda, Tamleugh, Violet Town
3670	Baddaginnie, Warrenbayne
3671	Benalla
3672	Benalla
3673	Benalla, Lima, Molyullah, Swanpool, Tatong, Winton
3675	Glenrowan, Greta, Hansonville
3676	Wangaratta
3677	Appin Park, Wangaratta, Yarrunga
3678	Boorhaman, Cheshunt, Everton, Milawa, Oxley
3682	Norong, Springhurst
3683	Chiltern
3685	Boorhaman North, Browns Plains, Gooramadda, Prentice North, Rutherglen
3687	Wahgunyah
3688	Barnawartha
3689	Wodonga
3690	Wodonga, Wodonga Plaza
3691	Allans Flat, Baranduda, Bellbridge, Berringama, Bethanga, Bonegilla, Dederang, Ebden, Glen Creek, Gundowring, Hume Weir, Kergunyah, Kiewa, Leneva, Lone Pine, Lucyvale, Mount Alfred, Staghorn Flat, Talgarno, Tangambalanga
3694	Bandiana Milpo
3695	Charleroi, Huon, Red Bluff, Sandy Creek
3697	Tawonga
3698	Tawonga South
3699	Bogong, Falls Creek, Mount Beauty
3700	Tallangatta
3701	Dartmouth, Eskdale, Granya, Mitta Mitta, Shelley
3704	Koetong
3705	Cudgewa, Nariel Valley
3707	Biggara, Colac Colac, Corryong, Thowgla Valley, Towong
3708	Tintaldra
3709	Burrowye, Guys Forest, Walwa
3711	Buxton
3712	Rubicon, Thornton
3713	Eildon
3714	Acheron, Alexandra, Cathkin, Koriella, Taggerty
3715	Ancona, Merton, Woodfield
3717	Flowerdale, Glenburn, Homewood, Murrindindi, Yea
3718	Molesworth
3719	Gobur, Kanumbra, Yarck
3720	Bonnie Doon
3722	Mansfield, Mirimbah
3723	Goughs Bay, Jamieson, Matlock, Merrijig, Mount Buller, Woods Point
3724	Mansfield
3725	Boxwood, Goorambat
3726	Bungeet, Devenish, Thoona
3727	Lake Rowan, St James, Yundool
3728	Tungamah, Wilby
3730	Bundalong, Telford, Yarrawonga
3732	Moyhu
3733	Whitfield, Whitlands
3735	Bowmans Forest, Whorouly
3736	Myrtleford
3737	Buffalo River, Dandongadale, Gapsted, Mudgegonga, Myrtleford, Rosewhite
3738	Ovens
3739	Eurobin
3740	Mount Buffalo, Porepunkah
3741	Bright, Freeburgh, Harrietville, Hotham Heights, Mount Hotham
3744	Wandiligong
3746	Eldorado
3747	Baarmutha, Beechworth, Murmungee, Stanley, Wooragee
3749	Yackandandah
3750	Wollert
3751	Woodstock
3752	South Morang
3753	Beveridge
3754	Doreen, Mernda
3755	Yan Yean
3756	Darraweit Guim, Hidden Valley, Upper Plenty, Wallan
3757	Eden Park, Humevale, Kinglake West, Pheasant Creek, Whittlesea
3758	Heathcote Junction, Wandong
3759	Panton Hill
3760	Smiths Gully
3761	St Andrews
3762	Bylands
3763	Kinglake
3764	Kilmore
3765	Montrose
3766	Kalorama
3767	Mount Dandenong
3770	Coldstream, Gruyere
3775	Christmas Hills, Dixons Creek, Steels Creek, Yarra Glen
3777	Healesville, Toolangi
3778	Narbethong
3779	Marysville
3781	Cockatoo
3782	Avonsleigh, Clematis, Emerald, Macclesfield
3783	Gembrook
3786	Ferny Creek
3787	Sassafras, Sassafras Gully
3788	Olinda
3789	Sherbrooke
3791	Kallista
3792	The Patch
3793	Monbulk
3795	Silvan
3796	Mount Evelyn
3797	Gilderoy, Powelltown, Three Bridges, Yarra Junction
3799	Mcmahons Creek, Millgrove, Warburton, Wesburn
3800	Monash University
3802	Endeavour Hills
3803	Hallam
3804	Narre Warren East, Narre Warren North
3805	Fountain Gate, Narre Warren, Narre Warren South
3806	Berwick, Harkaway
3807	Beaconsfield, Guys Hill
3808	Beaconsfield Upper
3809	Officer
3810	Pakenham, Pakenham Upper
3812	Maryknoll, Nar Nar Goon
3813	Tynong
3814	Cora Lynn, Garfield, Vervale
3815	Bunyip, Iona, Tonimbuk
3816	Labertouche, Longwarry, Modella
3818	Athlone, Drouin, Ripplebrook
3820	Warragul
3821	Buln Buln, Neerim Junction, Neerim North, Nilma, Rokeby
3822	Darnum
3823	Yarragon
3824	Childers, Thorpdale South, Trafalgar
3825	Aberfeldy, Coalville, Erica, Hernes Oak, Hill End, Moe, Moondarra, Newborough, Rawson, Tanjil South, Walhalla, Willow Grove, Yallourn North
3831	Neerim, Neerim South
3832	Neerim
3833	Noojee
3835	Thorpdale
3840	Jeeralang, Mid Valley, Morwell
3841	Gippsland Mc
3842	Churchill
3844	Callignee, Carrajung, Flynn, Koornalla, Traralgon, Tyers, Willung South
3847	Nambrok, Rosedale, Willung
3850	Guthridge, Sale, Wurruk
3851	Bundalaguah, Darriman, Kilmany, Loch Sport, Longford, Myrtlebank, Paradise Beach, Seaspray
3852	East Sale Raaf
3853	Sale
3854	Glengarry
3856	Toongabbie
3857	Cowwarr
3858	Glenmaggie, Heyfield, Licola, Seaton
3859	Newry, Tinamba
3860	Boisdale, Briagolong, Maffra, Valencia Creek
3862	Dargo, Meerlieu, Stratford
3864	Fernbank
3865	Lindenow
3869	Jumbuk, Yinnar
3870	Boolarra
3871	Darlimurla, Mirboo North
3873	Gormandale
3874	Carrajung South, Woodside
3875	Bairnsdale, Bengworden, Calulu, Hillside, Lindenow South, Lucknow, Mount Taylor, Newlands Arm, Sarsfield, Walpa, Wy Yung
3878	Eagle Point
3880	Paynesville, Raymond Island
3882	Nicholson
3885	Bruthen, Buchan, Butchers Ridge, Gelantipy, Mossiface, Tambo Upper, W Tree, Wiseleigh, Wulgulmerang
3886	Newmerella
3887	Lake Tyers, Nowa Nowa, Wairewa
3888	Bendoc, Bonang, Marlo, Orbost, Tubbut
3889	Bemm River, Cabbage Tree Creek, Club Terrace, Combienbar
3890	Cann River, Noorinbee
3891	Genoa, Gipsy Point
3892	Mallacoota
3893	Tambo Crossing
3895	Ensay
3896	Swifts Creek
3898	Dinner Plain, Omeo
3900	Benambra
3902	Johnsonville
3903	Swan Reach
3904	Metung
3909	Kalimna, Lake Tyers Beach, Lakes Entrance
3910	Langwarrin
3911	Baxter
3912	Pearcedale, Somerville
3913	Tyabb
3915	Hastings, Tuerong
3916	Merricks, Shoreham
3918	Bittern
3919	Crib Point
3920	Hmas Cerberus
3921	Tankerton
3922	Cowes
3923	Rhyll
3925	Cape Woolamai, Newhaven, San Remo
3926	Balnarring, Merricks Beach, Merricks North
3927	Somers
3928	Main Ridge
3929	Flinders
3930	Kunyung, Mount Eliza
3931	Mornington
3933	Moorooduc
3934	Mount Martha
3936	Arthurs Seat, Dromana, Safety Beach
3937	Red Hill, Red Hill South
3938	Mccrae
3939	Fingal, Rosebud
3940	Rosebud West
3941	Rye, St Andrews Beach, Tootgarook
3942	Blairgowrie
3943	Sorrento
3944	Portsea
3945	Jeetho, Krowera, Loch, Woodleigh
3946	Bena
3950	Korumburra
3951	Jumbunna, Kardella, Kongwak, Outtrim
3953	Berrys Creek, Hallston, Leongatha, Nerrena
3954	Koonwarra
3956	Dumbalk, Meeniyan, Tarwin, Venus Bay, Walkerville, Walkerville South
3957	Stony Creek
3958	Buffalo
3959	Fish Creek, Sandy Point, Waratah Bay
3960	Bennison, Foster, Mount Best, Tidal River, Yanakie
3962	Agnes, Toora
3964	Port Franklin
3965	Port Welshpool
3966	Binginwarri, Welshpool
3967	Hedley
3971	Alberton, Balook, Devon North, Gelliondale, Macks Creek, Port Albert, Tarraville, Won Wron, Yarram
3975	Lynbrook, Lyndhurst
3976	Hampton Park
3977	Cannons Creek, Cranbourne, Cranbourne East, Cranbourne North, Cranbourne South, Cranbourne West, Devon Meadows, Five Ways, Junction Village, Skye
3978	Cardinia, Clyde, Clyde North
3979	Almurta, Glen Alvie, Kernot
3980	Blind Bight, Tooradin, Warneet
3981	Bayles, Catani, Dalmore, Heath Hill, Koo Wee Rup, Yannathan
3984	Caldermeade, Corinella, Coronet Bay, Grantville, Jam Jerrup, Lang Lang, Monomeith, Tenby Point, The Gurdies
3987	Nyora
3988	Poowong
3990	Glen Forbes
3991	Bass
3992	Dalyston
3995	Archies Creek, Cape Paterson, Kilcunda, South Dudley, Wonthaggi, Woolamai
3996	Inverloch
8001	Melbourne
8002	East Melbourne
8003	Collins Street East
8004	St Kilda Road
8005	World Trade Centre
8006	Melbourne
8007	Collins Street West
8008	St Kilda Road Central
8009	Flinders Lane
8010	Law Courts
'''

def loadPostcodes():
    postCodes = {}
    try:
        #dataF = open("VictoriaPostcodes.csv", "r")
        dataF=VicPostcodeData.splitlines()
        #print dataF
        for s in dataF:
            code, names = s.split("\t")
            #print code, " = ", names
            for name in names.split(","):
                #print name.strip(), "=", code
                postCodes[name.strip()] = code.strip()
    except Exception as e:
        print('Exception', e);
    return postCodes;


"""
Main entry
"""
if __name__ == "__main__":
    postCodes = loadPostcodes()
    for suburb in ["Blackburn", "Blackburn North", "Blackburn South", "Viewbank"]:
        print suburb,"=",postCodes[suburb]