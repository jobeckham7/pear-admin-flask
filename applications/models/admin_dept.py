import datetime
from applications.extensions import db, ma
from marshmallow import fields, validate


class Dept(db.Model):
    __tablename__ = 'admin_dept'
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    parent_id = db.Column(db.Integer, comment="父级编号")
    dept_name = db.Column(db.String(50), comment="部门名称")
    sort = db.Column(db.Integer, comment="排序")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    remark = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')


class DeptSchema(ma.Schema):  # 序列化类
    deptId = fields.Integer(attribute="id")
    parentId = fields.Integer(attribute="parent_id")
    deptName = fields.Str(attribute="dept_name")
    leader = fields.Str()
    phone = fields.Str()
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    sort = fields.Integer()
