from dataclasses import dataclass, field


def stat_field(name: str, description: str = ""):
    return field(default=None, metadata={"name": name, "description": description})


@dataclass
class Stat:
    Level: int | None = stat_field("等级")
    MaxHP: int | None = stat_field(
        "体力上限",
        "该单位的最大生命值. 生命值降至0时，该单位从战斗中退场.",
    )
    AttackPower: int | None = stat_field(
        "攻击力",
        "影响：该单位进行攻击时，造成的伤害的量.",
    )
    DefensePower: int | None = stat_field(
        "防御力",
        "影响：该单位受到攻击时，受到的伤害的量.",
    )
    HealPower: int | None = stat_field(
        "治疗力",
        "影响：该单位的治疗技能可回复的生命值的量；该单位的护盾技能赋予的护盾可吸收伤害的量.",
    )
    AccuracyPoint: int | None = stat_field(
        "命中值",
        "影响：该单位进行攻击时，命中目标的概率.\n※ 该值高于目标的闪避值时，攻击必定命中.",
    )
    DodgePoint: int | None = stat_field(
        "闪避值",
        "影响：该单位受到攻击时，攻击命中的概率.\n※ 仅当该值高于攻击者的命中值时，攻击可以被闪避.",
    )
    CriticalPoint: int | None = stat_field(
        "暴击值",
        "影响：该单位进行攻击时，攻击暴击的概率.\n※ 仅当该值高于目标的暴击抵抗值时，攻击可以暴击.",
    )
    CriticalChanceRate: int | None = stat_field("暴击率加成")
    CriticalDamageRate: int | None = stat_field(
        "暴击伤害",
        "影响：该单位进行攻击时，攻击暴击造成的暴击伤害的量.\n※ 根据目标的暴伤抵抗率减少.",
    )
    HealEffectivenessRate: int | None = stat_field(
        "受恢复率",
        "影响：该单位受到回复时，回复的生命值的量.\n※ 不影响护盾效果.",
    )
    OppressionPower: int | None = stat_field(
        "群控强化",
        "影响：该单位对目标施加群控状态时，成功施加群控状态的概率.\n※ 也影响对部分敌方单位施加群控状态时，群控计量槽的填充量.",
    )
    OppressionResist: int | None = stat_field(
        "群控抵抗",
        "影响：该单位被施加群控状态时，成功被施加群控状态的概率.\n 也影响对部分敌方单位施加群控状态时，群控计量槽的填充量.",
    )
    CriticalChanceResistPoint: int | None = stat_field(
        "暴击抵抗力",
        "影响：该单位受到攻击时，攻击暴击的概率.\n※ 仅当该值低于攻击者的暴击值时，攻击可以暴击.",
    )
    CriticalDamageResistRate: int | None = stat_field(
        "暴击伤害抵抗率",
        "影响：该单位受到攻击时，攻击暴击造成的伤害的量.",
    )
    StabilityPoint: int | None = stat_field(
        "稳定值",
        "影响：该单位进行攻击时，造成的伤害的浮动区间的范围(造成伤害时在该范围内随机取1个值进行最终乘算).\n※ 该值越大，伤害浮动区间的左端点的值越大(即造成的最低伤害越大)",
    )
    StabilityRate: int | None = stat_field(
        "稳定率",
        "影响：该单位进行攻击时，造成的伤害的浮动区间的范围(造成伤害时在该范围内随机取1个值进行最终乘算).\n※ 该值越大，伤害浮动区间的左端点的值越大(即造成的最低伤害越大)",
    )
    Range: int | None = stat_field(
        "普通攻击射程",
        "影响：该单位对目标进行攻击时，可以进行普通攻击的最远距离.",
    )
    AmmoCount: int | None = stat_field(
        "装弹数",
        "该单位的武器的弹匣容量. 该单位进行普通攻击时消耗弹药数，弹药数降至0时进行换弹.",
    )
    AmmoCost: int | None = stat_field("普通攻击弹药消耗")
    MoveSpeed: int | None = stat_field(
        "移动速度",
        "影响：该单位的移动速度.",
    )
    DamageRatio: int | None = stat_field(
        "增伤率(敌)",
        "影响：该单位进行攻击时，造成的伤害的倍率.",
    )
    DamageRatio2: int | None = stat_field("增伤率")
    DamagedRatio: int | None = stat_field(
        "免伤率(敌)",
        "影响：该单位受到攻击时，受到的伤害的倍率",
    )
    DamagedRatio2: int | None = stat_field("免伤率")
    ExDamagedRatio: int | None = stat_field(
        "EX技能免伤率",
        "影响：该单位受到EX技能攻击时，受到的伤害的倍率.",
    )
    EnhanceExDamageRate: int | None = stat_field(
        "EX技能增伤率",
        "影响：该单位使用EX技能进行攻击时，造成的伤害的倍率",
    )
    EnhanceBasicsDamageRate: int | None = stat_field(
        "基础熟练度",
        "影响：该单位通过普通攻击、普通技能及子技能造成伤害时，造成的伤害的倍率.",
    )
    ReduceWeakDamagedRate: int | None = stat_field(
        "克制承伤率",
        "影响：该单位受到克制(显示Weak)攻击属性的攻击时，受到的伤害的倍率.",
    )
    HealRate: int | None = stat_field(
        "回复量加成",
        "影响：该单位通过技能回复生命值时，使目标回复生命值的倍率.",
    )
    AttackSpeed: int | None = stat_field(
        "攻击速度",
        "影响：该单位的 普攻准备时间、武器部署/回收时间、普攻持续时间、换弹时间、普攻前摇/后摇、普攻开火间隔 的持续时间.",
    )
    BlockRate: int | None = stat_field(
        "掩体格挡率",
        "影响：该单位处于掩体掩护下时，掩体成功格挡攻击的概率.",
    )
    DefensePenetration: int | None = stat_field(
        "防御无视值",
        "影响：该单位造成伤害时，无视目标防御力的量.",
    )
    RegenCost: int | None = stat_field(
        "蓄能值恢复力",
        "影响：该单位产生技能COST的速率.",
    )
    EnhanceExplosionRate: int | None = stat_field(
        "爆炸克制率",
        "影响：该单位进行攻击时，对轻型护甲防御属性的目标造成爆炸攻击属性伤害的量.",
    )
    EnhancePierceRate: int | None = stat_field(
        "贯通克制率",
        "影响：该单位进行攻击时，对重型装甲防御属性的目标造成贯通攻击属性伤害的量.",
    )
    EnhanceMysticRate: int | None = stat_field(
        "神秘克制率",
        "影响：该单位进行攻击时，对特殊装甲防御属性的目标造成神秘攻击属性伤害的量.",
    )
    EnhanceSonicRate: int | None = stat_field(
        "振动克制率",
        "影响：该单位进行攻击时，对弹性装甲防御属性的目标造成振动攻击属性伤害的量.",
    )
    EnhanceLightArmorRate: int | None = stat_field("轻型护甲性能")
    EnhanceHeavyArmorRate: int | None = stat_field("重型装甲性能")
    EnhanceUnarmedRate: int | None = stat_field("特殊装甲性能")
    EnhanceElasticArmorRate: int | None = stat_field("弹性装甲性能")
    ExtendBuffDuration: int | None = stat_field(
        "增益持续力",
        "影响：该单位对友方单位赋予增益状态时，增益状态的持续时间.",
    )
    ExtendDebuffDuration: int | None = stat_field(
        "减益持续力",
        "影响：该单位对敌方单位施加减益状态时，减益状态的持续时间.",
    )
    ExtendCrowdControlDuration: int | None = stat_field(
        "群控持续力",
        "影响：该单位对敌方单位施加群控状态时，群控状态的持续时间.",
    )
    SkillCost: int | None = stat_field("EX技能费用")
    NormalHits: int | None = stat_field("普通攻击伤害段数")
    EXHits: int | None = stat_field("EX技能伤害段数")
    PublicHits: int | None = stat_field("普通技能伤害段数")
    GroggyGauge: int | None = stat_field("虚弱计量槽")
    GroggyTime: int | None = stat_field("虚弱持续时间")
    LostHP: int | None = stat_field("已损生命值")
    CurrentHP: int | None = stat_field("当前生命值")
    TargetMaxHP: int | None = stat_field("目标生命值上限")
    BurnDamagedIncrease: int | None = stat_field("烧伤承伤率")
    ChillDamagedIncrease: int | None = stat_field("恶寒承伤率")
    ElectricShockDamagedIncrease: int | None = stat_field("触电承伤率")
    PoisonDamagedIncrease: int | None = stat_field("中毒承伤率")
    IgnoreDelayCount: int | None = stat_field(
        "无视普攻开火间隔",
        "该单位进行普通攻击时，无视的开火间隔的次数.",
    )
    MaxCostIncrease: int | None = stat_field("COST上限")
    SightPoint: int | None = stat_field(
        "视野",
        "影响：该单位判定遭遇到敌方单位的距离.",
    )

if __name__ == "__main__":
    from dataclasses import fields
    print(Stat.__dataclass_fields__["Level"].metadata["name"])

    # for f in fields(Stat):
    #     print(f.name, f.metadata["name"], f.metadata["description"])