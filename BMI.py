from import_lib import *


def BMI():
    with use_scope('BMI', if_exist='remove'):
        clear_scope('BMI')
        info = input_group(t('BMI calculation', '计算BMI：'), [
            input(t("Your Height(cm)", "请输入你的身高(cm)"), name="height", type=FLOAT),
            input(t("Your Weight(kg)", "请输入你的体重(kg)"), name="weight", type=FLOAT),
        ])

        BMI = info['weight'] / (info['height'] / 100) ** 2

        top_status = [(14.9, t('Severely underweight', '极瘦')), (18.4, t('Underweight', '偏瘦')),
                      (22.9, t('Normal', '正常')), (27.5, t('Overweight', '过重')),
                      (40.0, t('Moderately obese', '肥胖')), (float('inf'), t('Severely obese', '非常肥胖'))]

        for top, status in top_status:
            if BMI <= top:
                put_markdown(t('Your BMI: `%.1f`, Category: `%s`', '你的 BMI 值: `%.1f`，身体状态: `%s`') % (BMI, status))
                break
        #put_buttons(['返回首頁'], onclick=[whoAreYou])
        hold()