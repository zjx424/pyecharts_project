from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))#修改宽度，高度
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="商家A商家B", subtitle="商品"),toolbox_opts=opts.ToolboxOpts(is_show=True))
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render_notebook()