class CreateWertes < ActiveRecord::Migration[5.1]
  def change
    create_table :wertes do |t|
      t.float :temp
      t.float :humidity
      t.datetime :time

      t.timestamps
    end
  end
end
