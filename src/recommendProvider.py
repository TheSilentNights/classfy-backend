

topic = {
    "0": "已知一个直三棱柱的顶点都在一个球的球面上，该棱柱的底面为等腰直角三角形，且侧棱长与底面三角形的斜边长相等，现过球心作一截面，则截面的可能是;已知底面半径为r，高为2r的圆柱形容器内装有一半高度的水。现将一个半径为R的实心铁球放入容器中（铁球全部浸入水中），此时水面恰好上升至容器口齐平，则R/r=",
    "1": "已知三棱锥S-ABC中，SA=SB=SC=1，且SA、SB、SC两两垂直，P是三棱锥S-ABC外接球的球面上一动点，则点P到平面ABC的距离的最大值是;四棱锥O-ABCD，底面菱形边长2，∠ABC=60°，OA=2，M为OA中点，P为CD中点。证明：MP∥平面OBC",
    "2": "设正方体ABCD-A1B1C1D1的棱长为2，E为线段A₁D₁的中点，F为线段CC₁上的一个动点，则存在F，使得点F到直线AE的距离为12/5是否正确;在四面体ABCD中，∠ABC=π/3，AB=4，BC=4√3，二面角A-BC-D的大小为π/6，在侧面△ABC诸边及内部有一动点P，满足点P到直线AB的距离等于点P到平面BCD的距离，则点P到直线AB的距离是否等于点P到直线BC的距离",
    "3": "四棱锥O-ABCD，底面菱形边长2，∠ABC=60°，OA=2，M为OA中点，P为CD中点。求三棱锥M-PAD体积。;正方体棱长3，M为BB₁三等分点，N为AB三等分点，求三棱锥A₁-D₁-MN外接球表面积",
    "4": "在我国古代数学名著《九章算术》中，将四个面都是直角三角形的四面体称为“鳖臑”，在鳖臑A−BCD中，CD⊥平面ABC，且AB=BD=CD，M为AD的中点，则二面角M−BC−D的正弦值为;已知正方体ABCD−A1B1C1D1中，点E，F，G分别为棱AA1，AB1，C1D1的中点，该正方体的棱所在直线与平面DEF所成的角都相等是否正确。",
}


def get_recommendations(category):
    match category:
        case "0":
            return topic["0"]
        case "1":
            return topic["1"]
        case "2":
            return topic["2"]
        case "3":
            return topic["3"]
        case "4":
            return topic["4"]
    return None

