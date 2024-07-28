from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(unique=True, primary_key=True, autoincrement=True)

    def __repr__(self) -> str:
        return f""
    
    @property
    def column_names(self) -> list[str]:
        return [column.name for column in self.__table__.columns]
    
    # def model_dump(self):
    #     return [value for value in self.__table__.columns.values()]
        
        # return {
        #     name: getattr(self.__table__.c, name) for name in self.column_names 
        # }
