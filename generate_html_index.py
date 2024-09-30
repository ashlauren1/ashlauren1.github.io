import os

# Directories
base_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io'
players_dir = os.path.join(base_dir, 'players')
teams_dir = os.path.join(base_dir, 'teams')
boxscores_dir = os.path.join(base_dir, 'boxscores')

# List of player usernames and team names, and game ids
player_usernames = [  
    "ahose01","buntimi01","burnsbr01","deangan01","druryja01","fastje01","jarvise01","kotkaje01","lemiebr01","martijo01","necasma01","noesest01","orlovdm01","pescebr01","skjeibr01","slavija01","staaljo01","teravte01","raantan01","carrisa01","drysdja01","fowleca01","groulbe01","gudasra01","henriad01","johnsro02","jonesma03","lacomja01","leasobr01","lyubuil01","mctavma01","mintypa01","silfvja01","stromry01","terrytr01","vatrafr01","zegratr01","dostalu01","bennja01","dadonev01","duchema01","faksara01","hakanja01","harleth01","heiskmi01","hintzro01","johnswy01","lindees01","lundkni01","marchma01","paveljo01","roberja01","seguity01","smithcr01","steelsa01","suterry01","oettija01","carlsle01","luneatr01","gibsojo02","beechjo01","brownpa02","carlobr01","coylech01","debruja01","fredetr01","geekimo01","grzelma01","laukoja01","lindhha01","marchbr03","mcavoch01","mitchia01","pastrda01","poitrma01","shattke01","vanrija01","zachapa01","ullmali01","vaakaur01","bjugsni01","boydtr01","carcomi01","coolelo01","crousla01","dermotr01","dumbama01","durzise01","haytoba01","kellecl01","kerfoal01","maccema01","mcbaija03","moserja01","obrieli01","schmani01","stechtr01","valimju01","vejmeka01","amadimi01","barbaiv01","carriwi01","cottepa01","dorofpa01","eicheja01","howdebr01","huttobe01","karlswi01","koleske01","korczka01","audymjo01","mcnabbr01","pachabr01","pietral01","stephch02","stonema01","theodsh01","thomplo01","killoal01","acciano01","crosbsi01","ellerla01","gravery01","guentja01","hinosvi01","karlser01","letankr01","malkiev01","nietoma01","oconndr01","pettema01","rakelri01","ruhwech01","rustbr01","sheary01","smithre01","zohorra01","hellbma01","jarrytr01","atkinca01","belpelo01","brinkbo01","catesno01","coutuse01","deslani01","farabjo01","foersty01","frostmo01","hathaga01","konectr01","laughsc01","sanhetr01","seeleni01","tippeow01","walkese01","yorkca01","zamulye01","erssosa01","addisca01","burroky01","carpery01","eklunwi01","ferrama01","granlmi01","hertlto01","hoffmmi02","knyzhni01","kuninlu01","labanke01","okhotni01","ruttaja02","smithgi01","sturmni01","vlasima01","zadinfi01","zettefa01","blackma01","barkoal01","bennesa01","cousini01","ekblaaa01","ekmanol01","forslgu02","gadjojo01","kulikdm01","lombery01","lundean01","luostee01","mikkoni01","montobr01","reinhsa01","rodriev01","stenlke01","tkachma01","verhaca01","stolaan01","mcginbr01","alexani01","buchnpa01","faulkju01","hayeske01","kapanka01","krugto01","kyroujo01","leddyni01","neighja01","parayco01","perunsc01","saadbr01","scandma01","schenbr01","sundqos01","thomaro01","toropal01","vranaja01","hoferjo01","anderjo05","barroju01","caufico01","dvorach01","evansja02","gallabr01","guhleka01","kovacjo01","lindsgu01","mathemi01","monahse01","newhoal01","pearsta01","pezzemi01","slafkju01","strubja01","suzukni01","yloneje01","montesa01","andermi02","anderja01","byfiequ01","danauph01","doughdr01","duboipi01","engluan01","fialake01","gavrivl01","grundca01","kaliyar01","kempead01","kopitan01","laferal01","lewistr01","mooretr01","royma04","spencjo01","talboca01","aubekni01","carlsjo01","dowdni01","edmunjo01","feherma01","jenseni02","kuzneev01","lapiehe01","malenbe01","manthan01","mcmicco01","milanso01","ovechal01","protaal01","sandira01","stromdy01","vanritr01","wilsoto01","kuempda01","byrambo01","coglian01","coltoro01","drouijo01","johanry01","johnsja02","jonesca01","kivirjo01","mackina01","makarca01","mansojo01","nichuva01","oconnlo01","olofsfr01","rantami01","tatarto01","toewsde01","woodmi01","prosviv01","applema01","barromo01","connoky01","demeldy01","dillobr01","ehlerni01","gustada01","iafalal01","lowryad01","morrijo04","namesvl01","niedeni01","perfeco01","pionkne01","sambedy01","scheima01","stanllo01","vilarga01","helleco01","anderra01","backlmi01","colembl01","desimni01","dubedi01","gilbede01","greeraj01","hanifno01","huberjo01","kadrina01","lindhel01","mangian01","pospima01","ruzicad01","sharaye01","tanevch01","weegama01","zaryco01","marksja02","beniema01","bjorkol01","borgewi01","dumoubr01","dunnvi02","eberljo01","evansry01","gourdya01","kartyty01","larssad01","mccanja01","oleksja01","shorede01","tanevbr01","tolvaee01","wennbal01","yamamka01","daccojo01","hagueni01","martial01","royni01","whiteza01","kessemi01","sanfoza01","zuckeja01","ingraco01","bouchev01","brownco02","cecico01","deshavi01","draisle01","ekholma01","ernead01","foegewa01","hamblja01","hymanza01","janmama02","kaneev01","kulakbr01","mcdavco01","mcleory01","nugenry01","nurseda01","ryande01","pickaca01","benoisi01","bertuty01","broditj01","domima01","giordma01","gregono01","holmbpo01","jarnkca01","kampfda01","kniesma01","liljeti01","marnemi01","matthau01","mccabja01","mcmanbo02","nylanwi01","riellmo01","tavarjo01","jonesma02","lundeis01","jonssax01","schmina01","tonindo01","brossla01","chiarbe01","comphj.01","coppan01","debrial01","fabbrro01","fischch01","gostish01","kanepa01","larkidy01","maattol01","perroda01","petryje01","rasmumi01","raymolu01","seidemo01","spronda01","velenjo01","walmaja01","lyonal01","boninni01","brodzjo01","cuyllwi01","foxad01","goodrba01","gustaer02","kakkoka01","kreidch01","lafreal01","lindgry01","milleka01","panarar01","schnebr01","trochvi01","troubja01","veseyji02","wheelbl01","zibanmi01","shestig01","haggro01","bensoza01","cliftco01","cozendy01","dahlira01","girgeze01","greenjo02","johnsry03","jokihhe01","krebspe01","mitteca01","okposky01","peterjo01","powerow01","quinnja01","samuema02","skinnje01","thompta01","tuchal01","luukkuk01","zellwol01","baileju01","barabal01","coutulo01","duclaan01","macdoja02","mukhash01","kahkoka01","hollody01","perryco01","beanja01","boqviad01","chinaye01","danfoju01","gaudrjo01","gudbrer01","jennebo01","johnske01","kuralse01","marchki01","olivima01","provoiv01","rosloja01","severda01","sillico01","texieal01","vorondi01","werenza01","merzlel01","tarasda02","carrial01","evanglu01","fabbrda01","forsbfi01","glassco01","jankoma01","josiro01","lauzoje01","mccarmi01","mcdonry01","novakth01","nyquigu01","oreilry01","schenlu01","sherwki01","sissoco01","smithco02","treniya01","lankike01","bahlke01","brattje01","haulaer01","hischni01","holtzal01","hugheja03","hughelu01","lazarcu01","marinjo01","meierti01","merceda01","milleco02","nemecsi01","palaton01","siegejo01","smithbr05","tiernch01","toffoty01","dawsni01","schmiak01","bluegte01","boesebr01","coleia01","digiuph01","friedma01","garlaco01","hoglani01","hronefi01","hughequ01","juulsno01","laffesa01","mikheil01","millejt01","petteel01","podkova01","suterpi01","zadorni01","desmica01","bathedr01","bernaja01","branner01","chaboth01","chartro01","chychja01","giroucl01","greigri01","highmma01","josepma01","kastema01","kellypa01","kubaldo01","pintosh01","sandeja01","stuetti02","tkachbr01","zubar01","sogaama01","gawdigl01","regenpa01","dellaty01","stanklo01","meyerbe01","ahose02","barzama01","cizikca01","cluttca01","dobsono01","engvapi01","holmssi01","horvabo01","leean01","macleky01","martima02","nelsobr01","pageaje01","palmiky01","pelecad01","pulocry01","reillmi01","romanal01","varlasi01","beckmad01","bogosza01","boldyma01","brodijo01","chishde01","faberbr01","foligma01","gaudrfr01","hartmry01","johanma03","kapriki01","khusnma01","lucchja01","merrijo01","middlja01","rossima01","shawma01","zuccama01","gustafi01","anderjo08","athanan01","bedarco01","dickija01","donatry01","foligni01","johnsty01","jonesse01","kaisewy01","korchke01","kurasph01","megnaja02","raddyta01","reichlu01","slaggla01","tinorja01","vlasial01","zaitsni01","soderar01","cernaer01","cirelan01","dehaaca01","eyssimi01","glendlu01","hagelbr01","jeannta01","kucheni01","martiem01","mottety01","paulni01","perbini01","raddyda01","shearco01","stamkst01","watsoau01","johanjo03","bellepi01","burakan01","fleurca01","schulju01","schwaja01","wrighsh01","grubaph01","lageswi01","nesteni02","blaissa01","bolduza01","deanza01","kessema01","tuckety01","walkena01","binnijo01","arvidvi01","lizotbl01","thomaak01","coronma01","duehrwa01","huntdr01","kuzmean01","kylinol01","miromda01","rooneke01","wolfdu01","colansa01","copleph01","brownjo01","entwima01","johnsre01","murphco02","phillis01","mrazepe01","armiajo01","harrijo01","harvera01","xhekaar01","allenja01","kuparra01","kelemmi01","jenikja01","barreal01","fleurha01","hedmavi01","koepkco01","pointbr01","sergami01","georgal01","phillma01","lindgch01","lycksol01","ristora01","hartca01","thrunhe01","johnser01","jostty01","olofsvi01","robiner01","crookan01","hamontr01","norrijo01","smejkji01","tarasvl01","korpijo01","macdeku01","malinsa01","lockwwi01","bobrose01","boldusa01","gauthju01","mayfisc01","sorokil01","guentdy01","kirklju01","boqvije01","heineda01","lohrema01","wothepa01","swaymje01","oestejo01","barrity01","guriade01","parssju01","sarosju01","carteje01","harkija01","joseppi01","puustva01","whiteco02","brissbr01","rondbjo01","hillad01","dewarco01","duhaibr01","eriksjo02","lettivi01","mermida01","fleurma01","chatfja01","svechan01","kochepy01","villama01","gagnesa01","skinnst01","lajoima01","rifaima01","roberni01","samsoil01","beauvan01","blackco01","kochpa01","hollju01","sodervi01","hataksa01","nosekto01","leonajo01","crottca01","anglety01","chrisja01","gauncbr01","malatja01","meyerca01","pyyhtmi01","doanjo01","stastsp01","jonesza01","quickjo01","amanni01","joshuda01","myersty01","soucyca01","silovar01","brobeph01","kolyavl01","ratyak01","guttmco01","hallta02","katchbo01","forbode01","lucicmi01","tomasph01","czarnau01","kostikl01","hussovi01","steenos01","balinuv01","lorenst01","mahurjo01","klingjo01","reavery01","faschhu01","wahlsol01","bennima01","emberty01","fantiad01","jiricda01","lainepa01","martisp01","rosenis01","levide01","pitlity01","goligal01","huntda01","maroopa01","bastina01","mcleomi01","vanecvi01","merkuge01","nedelal01","myersph01","thompja01","vasilan02","bowersh01","willmma01","girarsa01","polinja01","royjo01","savarda01","stephmi01","primeca01","pelleja01","demkoth01","bearet01","oshietj01","pacioma01","sgarbmi01","richaan01","chaffmi01","clarkbr02","turcoal02","rittida01","hanlejo01","petroal01","poulide01","brazeju01","froesby01","morelma01","rempash01","wolljo01","bemstem01","grudejo02","ludvijo01","puljuje01","attarro01","poehlry01","staalma01","sandsfe01","peekean01","ostapza01","rempema01","macewza01","forsban01","megnaja01","chytifi01","merelwa01","vladada01","comrier01","lehkoar01","brysoja01","birobr01","rouselu01","spurgja01","savoima01","nylanal01","murrabr02","blankni01","timmico01","sabousc01","pitlire01","crozima01","rosenca01","denisgr01","berggjo02","reimeja01","alexeal01","mirosiv01","fedotiv01","ioriovi01","claguka01","anderfr01","peterja01","snivejo01","paterji01","borturo01","ponomva01","peretya01","raskaad01","dowliju01","parisza01","crevilo01","ginniad01","edvinsi01","subbama01","foudyli01","tomkima01","fixwotr01","greavje01","petanni01","footeca01","edstrad01","guenema01","bordeth01","chronma01","poulisa01","stivajo01","butleca01","foudyje01","wagnech01","annunju01","blakeja02","coghldy01","comtoma01","morrosc02","nadeabr01","brindga01","delbelu01","solovil01","delgama01","karlsli01","wedgesc01","driedch01","kuzneya01","klapkad01","schwico01","moverja01","grafco01","gushcda01","studnja01","coolede01","romange01","hamildo01","poturan01","mcginhu01","roosfi01","heineem01","seneybr01","bourqma01","wallsje01","delmaet01","nazarfr01","burkeca01","tufteri01","pavelon02","wintery01","olausos01","bjornto01","cormilu01","fagemsa01","bainsar01","andraem01","astonza01","dubepi01","hutsola01","hirosak01","lavoira01","campbja01","mintefr01","sourdju01","samosma01","johnsma04","maceama01","imamabo01","metevi01","peterca01","lindko01","ohgreli01","walkesa01","carlide01","murrama03","appleke01","klevety01","dachki01","backsni02","hamanha01","mccorma01","othmabr01","kempph01","condolu01","gignabr01","mailllo01","shepahu01","johanlu01","kulicji01","huttogr01","labersa01","hutchmi01","clarkgr01","halonbr01","footeno01","askarya01","afanaeg01","mclauma01","iskharu01","dominlo01","haydejo01","scanlbr01","matinni01","jarvero01","studema01","mackeco01","khairju01","koppajo01","gardnrh01","mcilrdy01","morrilo01","olofsgu01","szubema01","leschja01","gaudead01","goncaga01","steeval02","mcwarco01","lindbos01","gauthcu01","chibrni01","lambebr01","nashri02","blidhan01"
]
team_names = ["ANA", "ARI", "BOS", "BUF", "CAR", "CBJ", "CGY", "CHI", "COL", "DAL", "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NJD", "NSH", "NYI", "NYR", "OTT", "PHI", "PIT", "SEA", "SJS", "STL", "TBL", "TOR", "VAN", "VEG", "WPG", "WSH"]
game_ids = [
    "202310140VEG","202310150ANA","202310190ANA","202310210ARI","202310220ANA","202310240CBJ","202310260BOS","202310280PHI","202310300PIT","202311010ANA","202311050ANA","202311070ANA","202311100ANA","202311120ANA","202311140NSH","202311150COL","202311170ANA","202311190ANA","202311220ANA","202311240ANA","202311260EDM","202311280VAN","202311300ANA","202312020ANA","202312050COL","202312070CHI","202312100ANA","202312130NYI","202312150NYR","202312170NJD","202312180DET","202312210ANA","202312230ANA","202312270ANA","202312290ANA","202312310ANA","202401030ANA","202401050ANA","202401070ANA","202401090NSH","202401110CAR","202401130TBL","202401150FLA","202401160WSH","202401200SJS","202401210ANA","202401230ANA","202401250DAL","202401270MIN","202401310ANA","202402090ANA","202402130MTL","202402150OTT","202402170TOR","202402190BUF","202402210ANA","202402240LAK","202402250ANA","202402290SJS","202403010ANA","202403030ANA","202403060ANA","202403080ANA","202403100ANA","202403120CHI","202403140MIN","202403150WPG","202403170STL","202403190ANA","202403210ANA","202403240ANA","202403260SEA","202403280SEA","202403300EDM","202403310VAN","202404020CGY","202404050ANA","202404070ANA","202404090ANA","202404120ANA","202404130LAK","202404180VEG","202310130NJD","202310160NYR","202310170NYI","202310190STL","202310240LAK","202310270ARI","202310300ARI","202311020ARI","202311040ARI","202311070ARI","202311090STL","202311110NSH","202311140DAL","202311160CBJ","202311180WPG","202311200ARI","202311220ARI","202311250VEG","202311280ARI","202311300ARI","202312020ARI","202312040ARI","202312070ARI","202312090BOS","202312110BUF","202312120PIT","202312150ARI","202312160ARI","202312190ARI","202312210SJS","202312230COL","202312270ARI","202401020ARI","202401040ARI","202401070ARI","202401090ARI","202401110ARI","202401130MIN","202401160CGY","202401180VAN","202401200ARI","202401220ARI","202401240FLA","202401250TBL","202401270CAR","202402080ARI","202402100NSH","202402120PHI","202402140ARI","202402160ARI","202402180COL","202402190ARI","202402210ARI","202402250WPG","202402270MTL","202402290TOR","202403010OTT","202403030WSH","202403050ARI","202403070ARI","202403080ARI","202403100CHI","202403120MIN","202403140DET","202403160ARI","202403200DAL","202403220ARI","202403240ARI","202403260ARI","202403280ARI","202403300ARI","202404030ARI","202404050ARI","202404070SJS","202404090SEA","202404100VAN","202404120EDM","202404140CGY","202404170ARI","202310110BOS","202310140BOS","202310190SJS","202310210LAK","202310240CHI","202310280BOS","202310300BOS","202311020BOS","202311040DET","202311060DAL","202311090BOS","202311110MTL","202311140BUF","202311180BOS","202311200TBL","202311220FLA","202311240BOS","202311250NYR","202311270CBJ","202311300BOS","202312020TOR","202312030BOS","202312070BOS","202312130NJD","202312150NYI","202312160BOS","202312190BOS","202312220WPG","202312230MIN","202312270BUF","202312300BOS","202312310DET","202401020CBJ","202401040BOS","202401060BOS","202401080COL","202401110VEG","202401130STL","202401150BOS","202401180BOS","202401200BOS","202401220BOS","202401240BOS","202401250OTT","202401270PHI","202402060BOS","202402080BOS","202402100BOS","202402130BOS","202402150BOS","202402170BOS","202402190BOS","202402210EDM","202402220CGY","202402240VAN","202402260SEA","202402290BOS","202403020NYI","202403040TOR","202403050BOS","202403070BOS","202403090BOS","202403110BOS","202403140MTL","202403160BOS","202403190BOS","202403210BOS","202403230PHI","202403260FLA","202403270TBL","202403300WSH","202404020NSH","202404040CAR","202404060BOS","202404090BOS","202404130PIT","202404150WSH","202404160BOS","202310120BUF","202310140NYI","202310170BUF","202310190BUF","202310210BUF","202310230BUF","202310240OTT","202310270NJD","202310290BUF","202311010PHI","202311030BUF","202311040TOR","202311070CAR","202311100BUF","202311110PIT","202311170WPG","202311190CHI","202311220WSH","202311240BUF","202311250NJD","202311270NYR","202311300STL","202312020CAR","202312030BUF","202312050BUF","202312090BUF","202312130COL","202312150VEG","202312190BUF","202312210BUF","202312230NYR","202312300BUF","202312310OTT","202401040MTL","202401060PIT","202401090BUF","202401110BUF","202401130BUF","202401150BUF","202401180BUF","202401200BUF","202401240LAK","202401270SJS","202402060BUF","202402100BUF","202402130BUF","202402150BUF","202402170MIN","202402210MTL","202402230CBJ","202402250BUF","202402270FLA","202402290TBL","202403020BUF","202403030BUF","202403060TOR","202403070NSH","202403090BUF","202403120BUF","202403140BUF","202403160DET","202403180SEA","202403190VAN","202403210EDM","202403240CGY","202403270BUF","202403290BUF","202403300BUF","202404020BUF","202404050BUF","202404070DET","202404090DAL","202404110BUF","202404130FLA","202404150TBL","202310110CAR","202310140LAK","202310170SJS","202310190SEA","202310210COL","202310240TBL","202310260CAR","202310270CAR","202310300PHI","202311020NYR","202311040NYI","202311100FLA","202311110TBL","202311150CAR","202311180CAR","202311220CAR","202311240CAR","202311260CAR","202311280PHI","202311300CAR","202312040WPG","202312060EDM","202312070CGY","202312090VAN","202312120OTT","202312140DET","202312150CAR","202312170CAR","202312190CAR","202312210PIT","202312230CAR","202312270NSH","202312280CAR","202312300TOR","202401020NYR","202401050WSH","202401060CAR","202401130CAR","202401150CAR","202401190CAR","202401210CAR","202401250CAR","202402060CAR","202402080CAR","202402100CAR","202402130DAL","202402170VEG","202402190CAR","202402220CAR","202402240CAR","202402270MIN","202402290CBJ","202403020CAR","202403070CAR","202403090NJD","202403100CAR","202403120CAR","202403140CAR","202403160TOR","202403170OTT","202403190NYI","202403210CAR","202403220WSH","202403240CAR","202403260PIT","202403280CAR","202403300MTL","202404050CAR","202404070CAR","202404120STL","202404140CHI","202404160CBJ","202310120CBJ","202310140CBJ","202310160CBJ","202310200CBJ","202310210MIN","202310260MTL","202310280CBJ","202310300DAL","202311020CBJ","202311040WSH","202311060FLA","202311090CBJ","202311110DET","202311120NYR","202311140CBJ","202311180WSH","202311190PHI","202311220CBJ","202311240NJD","202311290CBJ","202312010CBJ","202312050CBJ","202312070NYI","202312080CBJ","202312100CBJ","202312140TOR","202312160CBJ","202312210CBJ","202312230CBJ","202312270NJD","202312290CBJ","202401040PHI","202401060CBJ","202401090WPG","202401130CBJ","202401150CBJ","202401190CBJ","202401230EDM","202401250CGY","202401270VAN","202401280SEA","202401300STL","202402100CBJ","202402130OTT","202402170SJS","202402200LAK","202402250CBJ","202402280NYR","202403020CHI","202403040CBJ","202403050PIT","202403070CBJ","202403090CBJ","202403120MTL","202403140CBJ","202403160CBJ","202403170CBJ","202403190DET","202403220COL","202403230VEG","202403280PIT","202403300CBJ","202404010CBJ","202404040CBJ","202404060CBJ","202404090TBL","202404110FLA","202404130NSH","202310110CGY","202310140PIT","202310160WSH","202310220DET","202310240CGY","202310260CGY","202310290EDM","202311010CGY","202311040SEA","202311070CGY","202311100TOR","202311110OTT","202311140MTL","202311160CGY","202311180CGY","202311200SEA","202311220NSH","202311240DAL","202311250COL","202311270CGY","202311300CGY","202312020CGY","202312050CGY","202312090CGY","202312110COL","202312120VEG","202312140MIN","202312160CGY","202312180CGY","202312230LAK","202312270CGY","202312310CGY","202401020MIN","202401040NSH","202401060PHI","202401070CHI","202401090CGY","202401130VEG","202401180CGY","202401200CGY","202401230CGY","202401270CGY","202402080NJD","202402100NYI","202402120NYR","202402150CGY","202402170CGY","202402190CGY","202402240EDM","202402270CGY","202403020CGY","202403040CGY","202403070TBL","202403090FLA","202403120CGY","202403140CGY","202403160CGY","202403180CGY","202403230VAN","202403260CHI","202403280STL","202403300CGY","202404040WPG","202404060CGY","202404090SJS","202404110LAK","202404160VAN","202404180CGY","202310100PIT","202310140MTL","202310160TOR","202310190COL","202310210CHI","202310270VEG","202311040CHI","202311050CHI","202311090TBL","202311120FLA","202311160CHI","202311180NSH","202311240CHI","202311260CHI","202311280CHI","202311300DET","202312020WPG","202312030MIN","202312050CHI","202312090CHI","202312100CHI","202312120EDM","202312140SEA","202312170CHI","202312190CHI","202312220CHI","202312230STL","202312270CHI","202312290DAL","202312310DAL","202401020NSH","202401040NYR","202401050NJD","202401090CHI","202401110WPG","202401130CHI","202401160CHI","202401190CHI","202401220VAN","202401240SEA","202401250EDM","202402070CHI","202402090CHI","202402130CHI","202402150CHI","202402170CHI","202402210CHI","202402230CHI","202402250CHI","202402290CHI","202403040COL","202403090WSH","202403150CHI","202403170CHI","202403190LAK","202403230SJS","202403280OTT","202403300PHI","202404020NYI","202404060CHI","202404070CHI","202404100STL","202404120CHI","202404160VEG","202404180LAK","202310110LAK","202310140SJS","202310170SEA","202310240NYI","202310260PIT","202311010COL","202311040VEG","202311070COL","202311090COL","202311110COL","202311130SEA","202311180DAL","202311200NSH","202311220COL","202311240MIN","202311270COL","202312030LAK","202312070COL","202312090COL","202312160WPG","202312170COL","202312210COL","202312290STL","202312310COL","202401020COL","202401040DAL","202401060COL","202401100COL","202401130TOR","202401150MTL","202401160OTT","202401200PHI","202401240COL","202401260COL","202402050NYR","202402060NJD","202402100FLA","202402130WSH","202402150TBL","202402200COL","202402220DET","202402240COL","202402270COL","202403020NSH","202403060COL","202403080COL","202403130VAN","202403160EDM","202403190STL","202403240COL","202403260COL","202403280COL","202403300COL","202404040MIN","202404050EDM","202404070COL","202404090COL","202404130COL","202404140VEG","202404180COL","202310120DAL","202310170VEG","202310210DAL","202310240PIT","202310260DAL","202311020EDM","202311040VAN","202311110WPG","202311120MIN","202311200DAL","202311220DAL","202311280WPG","202312020DAL","202312040TBL","202312060FLA","202312070WSH","202312090DAL","202312110DAL","202312150DAL","202312160STL","202312180DAL","202312210DAL","202312230NSH","202312270STL","202401020DAL","202401060DAL","202401080MIN","202401100DAL","202401120DAL","202401160DAL","202401180PHI","202401200NJD","202401210NYI","202401230DET","202401270DAL","202402070TOR","202402100MTL","202402150NSH","202402170DAL","202402200NYR","202402220OTT","202402260DAL","202402290DAL","202403020DAL","202403050SJS","202403090LAK","202403120DAL","202403140DAL","202403160DAL","202403220DAL","202403260SJS","202403280VAN","202403300SEA","202404030DAL","202404110DAL","202404130DAL","202404170DAL","202310120NJD","202310140DET","202310180DET","202310210OTT","202310240DET","202310260DET","202310300NYI","202311020DET","202311070NYR","202311090DET","202311160OTT","202311170DET","202311220DET","202311260DET","202311290NYR","202312020MTL","202312070DET","202312090DET","202312120STL","202312160PHI","202312200WPG","202312220DET","202312230NJD","202312270MIN","202312290DET","202401020SJS","202401040LAK","202401110DET","202401130DET","202401140TOR","202401170FLA","202401210DET","202401250DET","202401270DET","202401310DET","202402100DET","202402130EDM","202402150VAN","202402190SEA","202402240DET","202402270DET","202402290DET","202403020DET","202403090VEG","202403170PIT","202403210DET","202403230NSH","202403260WSH","202403300FLA","202404010TBL","202404050DET","202404090DET","202404110PIT","202404130TOR","202404150DET","202404160MTL","202310110VAN","202310140EDM","202310170NSH","202310190PHI","202310210EDM","202310240MIN","202310260EDM","202311040EDM","202311060VAN","202311090SJS","202311110SEA","202311130EDM","202311150EDM","202311180TBL","202311200FLA","202311240WSH","202311280EDM","202311300WPG","202312080EDM","202312100EDM","202312140EDM","202312160EDM","202312190NYI","202312210NJD","202312220NYR","202312280SJS","202312300LAK","202401020EDM","202401060EDM","202401130MTL","202401160EDM","202401180EDM","202401270EDM","202402060VEG","202402100LAK","202402150STL","202402230EDM","202402260EDM","202402280EDM","202403020SEA","202403030EDM","202403100PIT","202403130EDM","202403190EDM","202403230TOR","202403240OTT","202403260WPG","202403280EDM","202404010STL","202404100EDM","202404130EDM","202404150EDM","202310120MIN","202310140WPG","202310160NJD","202310190FLA","202310210FLA","202310240FLA","202310280FLA","202311080WSH","202311140SJS","202311160LAK","202311240FLA","202311270OTT","202311280TOR","202311300MTL","202312020FLA","202312080FLA","202312120SEA","202312140VAN","202312210FLA","202312230FLA","202312270TBL","202312290FLA","202312300FLA","202401040VEG","202401090STL","202401110FLA","202401130FLA","202401190FLA","202401220NSH","202401260PIT","202401270NYI","202402060FLA","202402080FLA","202402140PIT","202402170TBL","202402200FLA","202402240FLA","202402290FLA","202403040NYR","202403050NJD","202403070FLA","202403160FLA","202403210FLA","202403230NYR","202403240PHI","202403280FLA","202404010TOR","202404020MTL","202404040OTT","202404090FLA","202404160FLA","202310170WPG","202310190MIN","202310280LAK","202310310TOR","202311020OTT","202311040PHI","202311080VEG","202311090LAK","202311110LAK","202311180LAK","202311250LAK","202311290LAK","202312070MTL","202312090NYI","202312100NYR","202312130LAK","202312160SEA","202312190SJS","202312200LAK","202312270LAK","202312280VEG","202401020LAK","202401070WSH","202401090TBL","202401180LAK","202401200LAK","202401220LAK","202401280STL","202401310NSH","202402150NJD","202402180PIT","202402220LAK","202402290VAN","202403030LAK","202403050LAK","202403070LAK","202403110LAK","202403130STL","202403200LAK","202403230LAK","202403250VAN","202404010WPG","202404030LAK","202404040SJS","202404060LAK","202404150LAK","202310140TOR","202310170MTL","202310260PHI","202310270WSH","202310290NJD","202311020MIN","202311040MIN","202311070NYI","202311090NYR","202311180OTT","202311190MIN","202311280MIN","202311300NSH","202312070VAN","202312100SEA","202312160MIN","202312180PIT","202312210MIN","202312300WPG","202312310MIN","202401040MIN","202401120MIN","202401150MIN","202401180TBL","202401230MIN","202401250MIN","202402090MIN","202402120VEG","202402190MIN","202402200WPG","202402240SEA","202402290NSH","202403020STL","202403030MIN","202403100MIN","202403160STL","202403230MIN","202403280MIN","202403300MIN","202404020MIN","202404060MIN","202404120VEG","202404130SJS","202404180MIN","202310110TOR","202310210MTL","202310240MTL","202310280MTL","202310300VEG","202311040STL","202311070MTL","202311120MTL","202311160MTL","202311240SJS","202312040MTL","202312100MTL","202312130MTL","202312160MTL","202312180WPG","202312310TBL","202401060MTL","202401100PHI","202401110MTL","202401170NJD","202401180OTT","202401230MTL","202401250MTL","202401270PIT","202402060WSH","202402110MTL","202402150NYR","202402170MTL","202402220PIT","202402240NJD","202403020TBL","202403050NSH","202403090MTL","202403210VAN","202403240SEA","202403280MTL","202404040MTL","202404060MTL","202404070NYR","202404090MTL","202404110NYI","202404130OTT","202310200NYI","202310250NJD","202311030STL","202311100NJD","202311140WPG","202311160PIT","202311180NJD","202311280NJD","202311300PHI","202312010NJD","202312050VAN","202312070SEA","202312190NJD","202312290OTT","202401030WSH","202401060NJD","202401110TBL","202401220NJD","202401270TBL","202402120NJD","202402130NSH","202402170NJD","202402200WSH","202402220NJD","202402250NJD","202402270SJS","202403070NJD","202403110NYR","202403170VEG","202403190NJD","202403210NJD","202403230NJD","202403240NYI","202403260TOR","202404020NJD","202404030NYR","202404060OTT","202404070NJD","202404090NJD","202404110TOR","202404130PHI","202404150NJD","202310100TBL","202310120NSH","202310190NYR","202310210NSH","202310240NSH","202310280NSH","202310310VAN","202311020SEA","202311090WPG","202311240STL","202311260NSH","202311280NSH","202312020NSH","202312070NSH","202312090TOR","202312120NSH","202312160NSH","202312190NSH","202312210PHI","202312300WSH","202401130NSH","202401150VEG","202401290OTT","202402170STL","202402200VEG","202402240SJS","202402270NSH","202403130WPG","202403160SEA","202403190NSH","202403260NSH","202404040NSH","202404060NYI","202404090NSH","202404150PIT","202310260NYI","202311020WSH","202311110NYI","202311150VAN","202311160SEA","202311220NYI","202311240OTT","202311250NYI","202312050NYI","202312110NYI","202312200WSH","202312270NYI","202312290NYI","202312310PIT","202401060VEG","202401090NYI","202401110NYI","202401160WPG","202401230NYI","202402050TOR","202402080NYI","202402130NYI","202402180NYI","202402200PIT","202402220STL","202402240NYI","202403050NYI","202403070SJS","202403160NYI","202403170NYR","202403230NYI","202403300TBL","202404010PHI","202404090NYI","202404130NYR","202404170NYI","202310210SEA","202310280VAN","202310300WPG","202311220PIT","202311240PHI","202312030NYR","202312050OTT","202312090WSH","202312120NYR","202312190TOR","202312270NYR","202312300TBL","202401080NYR","202401110STL","202401130WSH","202401140NYR","202401160NYR","202401180VEG","202401230SJS","202401260NYR","202401270OTT","202402070NYR","202402240PHI","202403020TOR","202403090NYR","202403140TBL","202403160PIT","202403190NYR","202403260NYR","202404010NYR","202404110NYR","202404150NYR","202310140OTT","202310150OTT","202310180OTT","202310280PIT","202311040OTT","202311080TOR","202311090OTT","202312020OTT","202312070OTT","202312140STL","202312170VEG","202312230OTT","202312270TOR","202401020VAN","202401040SEA","202401130OTT","202401200OTT","202401210PHI","202402100OTT","202402190TBL","202402240OTT","202402260WSH","202403020PHI","202403090SJS","202403120OTT","202403210OTT","202403300WPG","202404070WSH","202404110TBL","202310170PHI","202310240VEG","202311070SJS","202311180PHI","202312020PIT","202312040PHI","202312140PHI","202312280VAN","202312290SEA","202401080PHI","202401130WPG","202401150STL","202401230PHI","202402080PHI","202402100PHI","202402150TOR","202402250PIT","202402270PHI","202403010WSH","202403040PHI","202403090TBL","202403120PHI","202403140PHI","202403190PHI","202404160PHI","202310130WSH","202310210STL","202311040SJS","202311190PIT","202311250PIT","202311300TBL","202312060TBL","202312160TOR","202312300PIT","202401020PIT","202401110PIT","202401150PIT","202401200VEG","202402060PIT","202402100WPG","202402270VAN","202402290SEA","202403070PIT","202403140PIT","202404040WSH","202404060PIT","202404080TOR","202310100VEG","202310140STL","202310300TBL","202311180VAN","202311220SEA","202311240SEA","202311300TOR","202312090SEA","202401010SEA","202401110WSH","202401210SEA","202401260SEA","202401300SJS","202402220SEA","202403050WPG","202403080SEA","202403120SEA","202403140SEA","202403210VEG","202404010SJS","202404110SEA","202404140STL","202404160WPG","202310120SJS","202310260TBL","202310290WSH","202311020SJS","202311100VEG","202311160SJS","202311200VAN","202311250SJS","202311270SJS","202312100VEG","202312120SJS","202312230VAN","202401040SJS","202401060SJS","202401090TOR","202402140WPG","202402190SJS","202403210SJS","202403300STL","202404060SJS","202310240WPG","202310270VAN","202311070STL","202311140STL","202312040VEG","202312060STL","202312190TBL","202401040STL","202401180WSH","202401200STL","202401240VAN","202402130TOR","202402190STL","202402270WPG","202403250STL","202310190TBL","202310210TBL","202311060TOR","202311220TBL","202312120VAN","202312210TBL","202312230WSH","202401020WPG","202402220TBL","202403190VEG","202404030TOR","202404130WSH","202404170TBL","202310240WSH","202311110TOR","202401200VAN","202401240TOR","202401270WPG","202402220VEG","202402270TOR","202403200WSH","202403280TOR","202311300VAN","202402110WSH","202402170VAN","202403070VEG","202403090VAN","202403160VAN","202404020VEG","202404080VAN","202404180WPG","202310190WPG","202311020VEG","202311140WSH","202312020VEG","202403280WPG","202403110WPG","202403240WSH"
]

# Function to generate HTML list items
def generate_list_items(items, prefix):
    return "\n".join([f'<li><a href="{prefix}/{item}.html">{item}</a></li>' for item in items])

# Update players/index.html
players_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Player Directory</title>
</head>
<body>
    <main id="content">
        <h2>Player Directory</h2>
        <p>Browse through all players:</p>
        <ul>
            {generate_list_items(player_usernames, '/players')}
        </ul>
    </main>
</body>
</html>
"""
with open(os.path.join(players_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(players_content)
print("Updated players/index.html")

# Update teams/index.html
teams_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Directory</title>
</head>
<body>
    <main id="content">
        <h2>Team Directory</h2>
        <p>Browse through all teams:</p>
        <ul>
            {generate_list_items(team_names, '/teams')}
        </ul>
    </main>
</body>
</html>
"""
with open(os.path.join(teams_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(teams_content)
print("Updated teams/index.html")

# Update boxscores/index.html
boxscores_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boxscore Directory</title>
</head>
<body>
    <main id="content">
        <h2>Game Boxscores</h2>
        <p>Browse through all boxscores:</p>
        <ul>
            {generate_list_items(game_ids, '/boxscores')}
        </ul>
    </main>
</body>
</html>
"""
with open(os.path.join(boxscores_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(boxscores_content)
print("Updated boxscores/index.html")